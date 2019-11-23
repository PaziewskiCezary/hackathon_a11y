import json

import requests

from .api_key import YT_API_KEY

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
        return requests.get("https://www.googleapis.com/youtube/v3/{}"
                            .format(api),
                         {
                             "key": YT_API_KEY,
                             **kwargs
                         }).json()

    def search(self, phrase, max_results=25):
        """
        Requests search results of `phrase`

        :param phrase: str
        :param max_results: optional, default: 25
        :return: Dictionary
            "items" key contains a list of dictionaries representing the results
                there "id"["videoId"] contains the video or playlist id
        """
        r = self.__request("search", part="snippet",
            q=phrase, max_results="{}".format(max_results))

