import json
import os.path
import requests

from app.paths import APP_ROOT

REQUEST_URL = "https://api.genius.com/oauth/token"


class AccessUtil:
    def __init__(self):
        self.credentials_location = os.path.join(
            APP_ROOT, *["resources", "secrets", "genius-secret-key.json"]
        )
        self.access_token = None
        self.refresh_access_token()

    def get_access_token(self):
        return self.access_token

    def refresh_access_token(self):
        with open(self.credentials_location, "r") as secretIn:
            secret_json = json.load(secretIn)
            client_id = secret_json[u'client_id']
            client_secret = secret_json[u'client_secret']
            token_response = requests.post(REQUEST_URL, data={
                "client_id": client_id,
                "client_secret": client_secret,
                "grant_type": "client_credentials"
            })

            response_json = token_response.json()

            self.access_token =  response_json[u'access_token']
