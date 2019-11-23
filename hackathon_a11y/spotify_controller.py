import base64

import requests
import pyfy

from hackathon_a11y.api_key import SPOTIFY_CLIENT_ID, SPOTIFY_CLIENT_SECRET

class SpotifyController:
    def __init__(self):
        # Get access token
        s = "{}:{}".format(SPOTIFY_CLIENT_ID,
                       SPOTIFY_CLIENT_SECRET)
        token_request = "Basic {}".format(
            base64.b64encode(s.encode("utf-8")).decode())
        r = requests.post("https://accounts.spotify.com/api/token", data = {
            "grant_type" : "client_credentials"
        }, headers = {
            "Content-Type" : "application/x-www-form-urlencoded",
            "Authorization" : token_request
        })
        self.token = r.json()["access_token"]
