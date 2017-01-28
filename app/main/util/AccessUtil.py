import json
import os.path
import requests

REQUEST_URL = "https://api.genius.com/oauth/token"

def getAccessToken():
    credentialsLocation = os.path.join(
        os.path.dirname(__file__), '../../resources/secrets/genius-secret-key.json'
    )

    with open(credentialsLocation, "r") as secretIn:
        secretJson = json.load(secretIn)
        clientId = secretJson[u'clientId']
        clientSecret = secretJson[u'clientSecret']
        tokenResponse = requests.post(REQUEST_URL, data={
            "client_id": clientId,
            "client_secret": clientSecret,
            "grant_type": "client_credentials"
        })

        responseJson = tokenResponse.json()

        return responseJson[u'access_token']

