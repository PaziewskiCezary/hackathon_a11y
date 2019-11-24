from hackathon_a11y.main_view import MainView
from hackathon_a11y.youtube_list_view import YoutubeListView
from hackathon_a11y.youtube_view import YoutubeView

class ViewsController:
    def __init__(self):
        # This map exists to avoid circular imports
        self.views = {
            "Main" : MainView,
            "YoutubeList" : YoutubeListView,
            "Youtube" : YoutubeView
        }

    def start(self):
        mv = MainView(self)
        mv.display()

if __name__ == "__main__":
    vc = ViewsController()
    vc.start()