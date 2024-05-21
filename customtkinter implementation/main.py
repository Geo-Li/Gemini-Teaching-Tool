from configparser import ConfigParser

from alert_window import *
from login_window import *
# from search_window import * 
from selection_window import *
from gemini_window import *



def main() -> int:
    LoginWindow()
    # SearchWindow()
    # In the selection window, users will 
    # decide on which functionality to play with
    SelectionWindow()
    settings = ConfigParser()
    settings.read("config/settings.ini")
    function = settings["App"]["function"]
    # Load the decision and to see which window to open
    if function == "Bing Search":
        pass
    elif function == "Gemini":
        GeminiWindow()
    return 0



if __name__ == "__main__":
    main()
