from typing import Tuple, Union
from customtkinter import *
from configparser import ConfigParser
from time import sleep
from alert_window import AlertWindow


settings = ConfigParser()
settings.read("config/settings.ini")
FONT_INFO = settings["Font"]


class LoginWindow(CTk):
    def __init__(self,
                 fg_color: Union[str, Tuple[str, str], None] = None,
                 **kwargs):
        super().__init__(fg_color, **kwargs)
        font = CTkFont(family=FONT_INFO["family"], size=int(FONT_INFO["size"]))
        set_appearance_mode("Light")
        self.configure(fg_color="white")
        self.geometry("500x250")
        self.title("Login")

        title_frame = CTkFrame(master=self, fg_color="white")
        title = CTkLabel(master=title_frame,
                         text="Please enter your API info below",
                         font=font)
        title.cget("font").configure(size=font.cget("size")+8,
                                     weight="bold")
        title.pack()
        title_frame.pack(padx=10, pady=(10,0))

        api_input_frame = CTkFrame(master=self,
                                   fg_color="white")
        # api_input_frame.grid(row=0, column=0, sticky="ew", padx=20)
        api_input_frame.grid_columnconfigure(0, weight=1)
        api_input_frame.grid_columnconfigure(1, weight=2)
        bing_search_api_label = CTkLabel(master=api_input_frame,
                                         text="Bing Search API Key")
        bing_search_api_label.grid(row=0, column=0,
                                   sticky='e', padx=5, pady=10)
        self.bing_api_key = StringVar()
        bing_search_api_entry = CTkEntry(master=api_input_frame,
                                         placeholder_text="Copy & Paste your API key here",
                                         textvariable=self.bing_api_key)
        bing_search_api_entry.grid(row=0, column=1, sticky='ew')
        gemini_model_api_label = CTkLabel(master=api_input_frame,
                                          text="Gemini Model API Key")
        gemini_model_api_label.grid(row=1, column=0,
                                    sticky='e', padx=5, pady=10)
        self.gemini_api_key = StringVar()
        gemini_model_api_entry = CTkEntry(master=api_input_frame,
                                          placeholder_text="Copy & Paste your API key here",
                                          textvariable=self.gemini_api_key)
        gemini_model_api_entry.grid(row=1, column=1, sticky='ew')
        api_input_frame.pack(pady=10, padx=20,
                             fill='both', expand=True)

        window_options = CTkFrame(master=self, fg_color="white")
        self.confirm_button = CTkButton(window_options,
                                        text="Confirm",
                                        command=self.update_api_keys)
        self.cancel_button = CTkButton(window_options,
                                       text="Cancel",
                                       command=self.close)
        self.confirm_button.grid(row=0, column=0,
                                 padx=20)
        self.cancel_button.grid(row=0, column=1,
                                padx=20)
        window_options.pack(pady=(0,20))
        self.mainloop()


    def update_api_keys(self):
        if len(self.bing_api_key.get()) == 32 and len(self.gemini_api_key.get()) == 39:
            api_keys = ConfigParser()
            api_keys["API_Keys"] = {
                "bing_search_api": self.bing_api_key.get(),
                "gemini_model_api": self.gemini_api_key.get()
            }
            with open('api_keys.ini', 'w') as api_keys_file:
                api_keys.write(api_keys_file)
            message = "Bing Search and Gemini Model API keys have been set!"
            alertWindow = AlertWindow(message=message,
                                      callbacks={
                                          "change_button_text": self.change_button_text(text="Close")
                                      })
        else:
            message = "Please provide API keys for data processing!"
            alertWindow = AlertWindow(message=message)

    def close(self):
        sleep(0.25)
        self.destroy()

    def change_button_text(self, text):
        self.cancel_button.configure(text=text)



if __name__ == "__main__":
    loginWindow = LoginWindow()

