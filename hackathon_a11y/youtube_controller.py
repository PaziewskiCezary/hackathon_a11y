import requests

from .api_key import API_KEY

class YoutubeController:
    """
    Class to define methods to interact with YT API (and VLC?)

    """
    def __request(self, api, **kwargs):
        """
        Request to YouTube v3 API

        :param api: what to put after "googleapis.com/youtube/v3/"
        :param kwargs: request parameters, API-dependent
        :return: Content of the response, should be a JSON
        """
        r = requests.get("https://www.googleapis.com/youtube/v3/{}".format(api),
                         {
                             "key": API_KEY,
                             **kwargs
                         })

        return r

    def search(self, phrase):
        r = self.__request("channels", part="snippet,contentDetails,statistics",
            id="UC_x5XG1OV2P6uZZ5FSM9Ttw")

        print(r.content)
