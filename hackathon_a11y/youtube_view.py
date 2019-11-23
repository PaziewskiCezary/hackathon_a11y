from .youtube_controller import YoutubeController
from .view import View

class YoutubeView(View):
    """
    Class representing a window of YouTube app

    Static attribute:
        controller : YouTubeController
    """
    controller = YoutubeController()
