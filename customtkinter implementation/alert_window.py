from typing import Tuple, Union
from customtkinter import *
from configparser import ConfigParser
from time import sleep


settings = ConfigParser()
settings.read("config/settings.ini")
FONT_INFO = settings["Font"]


class AlertWindow(CTkToplevel):
    def __init__(self, 
                 message: str,
                 fg_color: Union[str, Tuple[str, str], None] = None, 
                 callbacks = None,
                 **kwargs):
        super().__init__(fg_color, **kwargs)
        font = CTkFont(family=FONT_INFO["family"], size=int(FONT_INFO["size"]))
        set_appearance_mode("Light")
        self.configure(fg_color="white")
        self.set_geometry(message=message)
        self.title("Alert")

        message_label = CTkLabel(master=self,
                                 text=message,
                                 font=font)
        message_label.pack(padx=20, pady=20)
        confirm_button = CTkButton(self,
                                   text="Confirm",
                                   command=self.close)
        confirm_button.pack(padx=20, pady=20)

        if callbacks:
            if "change_button_text" in callbacks:
                callbacks["change_button_text"]

        self.mainloop()

    
    def set_geometry(self, geometry: str = None, message: str = None):
        if message:
            dimention_x = ((len(message) // 10) + 1) * 100
            self.geometry(str(dimention_x) + "x150")
        else:
            self.geometry(geometry)


    def close(self):
        sleep(0.25)
        self.destroy()


if __name__ == "__main__":
    message = "This is a test message for the Alert Window"
    print(len(message))
    alertWindow = AlertWindow(message=message)