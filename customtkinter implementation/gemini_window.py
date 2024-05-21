from typing import Tuple, Union
from customtkinter import *
from configparser import ConfigParser
from time import sleep
from library.gemini_model import *
from alert_window import AlertWindow


settings = ConfigParser()
settings.read("config/settings.ini")
FONT_INFO = settings["Font"]


class GeminiWindow(CTk):
    def __init__(self,
                 **kwargs):
        super().__init__(**kwargs)
        font = CTkFont(family=FONT_INFO["family"], size=int(FONT_INFO["size"]))
        set_appearance_mode("Light")
        self.geometry("1000x500")
        self.configure(fg_color="white")
        self.title("Gemini")

        message_label = CTkLabel(master=self,
                                 text="Gemini",
                                 font=font)
        message_label.pack(padx=20, pady=20)
        chat_frame = CTkFrame(master=self,
                                fg_color="white")
        chat_frame.grid_columnconfigure(0, weight=5)
        chat_frame.grid_columnconfigure(1, weight=1)
        # Set up the chat box input entry
        self.chat_input = StringVar()
        chat_input_entry = CTkEntry(master=chat_frame,
                                placeholder_text="Let's chat!",
                                textvariable=self.chat_input)
        chat_input_entry.grid(row=0, column=0, sticky="we", padx=(20,0))

        send_button = CTkButton(master=chat_frame,
                                text="Send",
                                command=self.chat)
        send_button.grid(row=0, column=1)
        chat_frame.pack(fill="both", expand=True)

        self.result_text = StringVar()
        result_label = CTkLabel(master=self,
                                textvariable=self.result_text)
        result_label.pack(pady=(0, 50))

        # Initialize the Gemini component
        try:
            api_keys = ConfigParser()
            api_keys.read("config/api_keys.ini")
            gemini_model_api = api_keys["API_Keys"]["gemini_model_api"]
            if len(gemini_model_api) != 39:
                message = "Please provide the Gemini API key in the Login window"
                alertWindow = AlertWindow(message=message)
        except:
            message = "Please provide the Gemini API key in the Login window"
            alertWindow = AlertWindow(message=message)
        self.gemini_model = GeminiModel(gemini_model_api)
        

        self.mainloop()


    def chat(self):
        response = self.gemini_model.send_message(self.chat_input.get())
        self.result_text.set(response)


    def close(self):
        sleep(0.25)
        self.destroy()


if __name__ == "__main__":
    geminiWindow = GeminiWindow()
