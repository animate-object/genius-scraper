import requests
import logging

from app.main.util.access_util import AccessUtil
from app.main.util.exceptions import HttpException
from app.paths import LOG_DIR

logging.basicConfig(filename=LOG_DIR + "\\requests_log.txt", level=logging.INFO)


class RequestWrapper:
    def __init__(self, access_util=AccessUtil()):
        self.access_util = access_util

    def get_with_headers(self, url, payload, success_code=200, retry=False):
        logging.info("GET request to url {}".format(url))
        api_response = requests.get(url=url, data=payload, headers=self._get_headers())
        if api_response.status_code != success_code:
            if api_response.status_code == 401:
                if retry:
                    raise HttpException(
                        "HttpException on request. Request failed authentication on retry",
                        api_response.status_code,
                        api_response.json()
                    )
                else:
                    logging.info("Attempting to refresh access token.")
                    self.access_util.refresh_access_token()
                    logging.info("Access token refreshed.")
                    logging.info("Retrying request.")
                    api_response = self.get_with_headers(url, payload, success_code, retry=True)
            else:
                raise HttpException("HttpException on request", api_response.status_code, api_response.json())

        return api_response.json()

    def _get_headers(self):
        return {"Authorization": "Bearer {}".format(self.access_util.get_access_token())}
