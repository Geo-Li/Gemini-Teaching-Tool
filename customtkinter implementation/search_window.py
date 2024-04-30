from typing import Tuple, Union
from customtkinter import *
from configparser import ConfigParser
from time import sleep
from library.bing_search import *
from alert_window import AlertWindow


settings = ConfigParser()
settings.read("config/settings.ini")
FONT_INFO = settings["Font"]


class SearchWindow(CTk):
    def __init__(self,
                 fg_color: Union[str, Tuple[str, str], None] = None,
                 **kwargs):
        super().__init__(fg_color, **kwargs)
        font = CTkFont(family=FONT_INFO["family"], size=int(FONT_INFO["size"]))
        set_appearance_mode("Light")
        self.geometry("500x200")
        self.configure(fg_color="white")
        self.title("Search")

        message_label = CTkLabel(master=self,
                                 text="MyEdMaster",
                                 font=font)
        message_label.pack(padx=20, pady=20)
        self.search_input = StringVar()
        search_input_entry = CTkEntry(master=self,
                                placeholder_text="Copy & Paste your API key here",
                                textvariable=self.search_input,
                                width=300)
        search_input_entry.pack(padx=20, pady=20)

        confirm_button = CTkButton(self,
                                   text="Search",
                                   command=self.search)
        confirm_button.pack(padx=20, pady=20)

        try:
            api_keys = ConfigParser()
            api_keys.read("api_keys.ini")
            bing_search_api = api_key["API_Keys"]["bing_search_api"]
            if len(bing_search_api) != 32:
                message = "Please provide the Bing Search API key in the Login window"
                alertWindow = AlertWindow(message=message)
        except:
            message = "Please provide the Bing Search API key in the Login window"
            alertWindow = AlertWindow(message=message)


        self.mainloop()


    def search(self):
        pass


    def close(self):
        sleep(0.25)
        self.destroy()


if __name__ == "__main__":
    searchWindow = SearchWindow()