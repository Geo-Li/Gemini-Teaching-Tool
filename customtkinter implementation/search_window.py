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
                 **kwargs):
        super().__init__(**kwargs)
        font = CTkFont(family=FONT_INFO["family"], size=int(FONT_INFO["size"]))
        set_appearance_mode("Light")
        self.geometry("800x200")
        self.configure(fg_color="white")
        self.title("Search")

        message_label = CTkLabel(master=self,
                                 text="MyEdMaster",
                                 font=font)
        message_label.pack(padx=20, pady=20)
        search_frame = CTkFrame(master=self,
                                fg_color="white")
        search_frame.grid_columnconfigure(0, weight=5)
        search_frame.grid_columnconfigure(1, weight=1)
        # Set up the search input entry
        self.search_input = StringVar()
        search_input_entry = CTkEntry(master=search_frame,
                                placeholder_text="Ask me questions!",
                                textvariable=self.search_input)
        search_input_entry.grid(row=0, column=0, sticky="we", padx=(20,0))

        search_button = CTkButton(master=search_frame,
                                   text="Search",
                                   command=self.search)
        search_button.grid(row=0, column=1)
        search_frame.pack(fill="both", expand=True)

        # Initialize the Bing Search component
        try:
            api_keys = ConfigParser()
            api_keys.read("config/api_keys.ini")
            bing_search_api = api_keys["API_Keys"]["bing_search_api"]
            if len(bing_search_api) != 32:
                message = "Please provide the Bing Search API key in the Login window"
                alertWindow = AlertWindow(message=message)
        except:
            message = "Please provide the Bing Search API key in the Login window"
            alertWindow = AlertWindow(message=message)
        endpoint = "https://api.bing.microsoft.com/v7.0/search"
        self.bing_search_model = BingSearch(bing_search_api, endpoint)
            response = model.search({
                'q': "how to do matrix multiplication",
                'count': 50,
                'offset': 0,
                'mkt': 'en-US',
                'freshness': 'Month'
            })
            urls = model.parse_url(response)
            html = model.parse_html(urls, range(1))
            print(html)
        

        self.mainloop()


    def search(self):
        query = self.search_input.get()


    def close(self):
        sleep(0.25)
        self.destroy()


if __name__ == "__main__":
    searchWindow = SearchWindow()
