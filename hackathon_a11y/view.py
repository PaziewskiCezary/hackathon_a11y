from abc import abstractmethod

from user_settings import UserSettings


class View:
    """
    Abstract class to represent a window

    Static attribute:
        user_settings : UserSettings
            Containts info specific to user, e.g. time between elements
            to highlight

    Attributes:
        highlighted_element : GUI Element
        highlight_cycle : List[GUI Element]
            List of elements to highlight
        action_map : Dictionary GUI Element -> Function
            If key-event is detected, function action_map[highlighted_element]
            is called with highlighted_element as its argument
    """

    user_settings = UserSettings()


    @abstractmethod
    def display(self):
        """
        Creates and displays the window; starts highlightning cycle

        :return: None
        """
        pass

