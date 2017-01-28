import json
import os.path
import requests

REQUEST_URL = "https://api.genius.com/oauth/token"


def get_access_token():
    # TODO refactor to save current access token until it expires. May require rethinking around requests.
    credentials_location = os.path.join(
        os.path.dirname(__file__), '../../resources/secrets/genius-secret-key.json'
    )

    with open(credentials_location, "r") as secretIn:
        secret_json = json.load(secretIn)
        client_id = secret_json[u'client_id']
        client_secret = secret_json[u'client_secret']
        token_response = requests.post(REQUEST_URL, data={
            "client_id": client_id,
            "client_secret": client_secret,
            "grant_type": "client_credentials"
        })

        response_json = token_response.json()

        return response_json[u'access_token']

