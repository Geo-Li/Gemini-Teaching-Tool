from typing import Tuple, Union
from customtkinter import *
from configparser import ConfigParser
from time import sleep
from alert_window import AlertWindow


settings = ConfigParser()
settings.read("config/settings.ini")
FONT_INFO = settings["Font"]


class SelectionWindow(CTk):
    def __init__(self,
                 **kwargs):
        super().__init__(**kwargs)
        font = CTkFont(family=FONT_INFO["family"], size=int(FONT_INFO["size"]))
        set_appearance_mode("Light")
        self.geometry("600x300")
        self.configure(fg_color="white")
        self.title("Search")

        message_label = CTkLabel(master=self,
                                 text="Choose which service you want to use",
                                 font=font)
        message_label.pack(padx=20, pady=20)
        selection_frame = CTkFrame(master=self,
                                fg_color="white")
        # Set up two buttons for selection
        bing_search_button_text = "Bing Search"
        bing_search_button = CTkButton(master=selection_frame,
                                   text=bing_search_button_text,
                                   command=(
                                       lambda: self.select(bing_search_button_text)
                                    ))
        bing_search_button.pack(side="left", padx=10, expand=True)
        gemini_button_text = "Gemini"
        gemini_button = CTkButton(master=selection_frame,
                                text=gemini_button_text,
                                command=(
                                    lambda: self.select(gemini_button_text)
                                ))
        gemini_button.pack(side="right", padx=10, expand=True)
        selection_frame.pack(fill="both", expand=True)

        self.mainloop()


    def select(self, choice):
        settings = ConfigParser()
        settings.read("config/settings.ini")
        if not settings.has_section("App"):
            settings.add_section("App")
        settings.set("App", "function", choice)
        with open("config/settings.ini", 'w') as settings_file:
            settings.write(settings_file)
        sleep(0.25)
        self.destroy()



if __name__ == "__main__":
    selectionWindow = SelectionWindow()
