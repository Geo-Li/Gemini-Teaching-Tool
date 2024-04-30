import tkinter
import customtkinter

customtkinter.set_appearance_mode("System")
customtkinter.set_default_color_theme("blue")

def web_search(b: customtkinter.CTkEntry):
    print(b.get())

def checkbox_event(num):
    print("this is a number", num)

def main() -> int:
    app = customtkinter.CTk()
    app.geometry("720x480")

    title = customtkinter.CTkLabel(app, text="Gemini Project")
    title.pack(padx=10, pady=10)

    search_input = tkinter.StringVar()
    search_bar = customtkinter.CTkEntry(app, placeholder_text="What is your question", width=350, height=40, textvariable=search_input)
    search_bar.pack()
    i = search_bar.get()

    search_button = customtkinter.CTkButton(app, text="Search", command=web_search(search_bar))
    search_button.pack()

    check_var = customtkinter.StringVar(value="on")
    checkbox = customtkinter.CTkCheckBox(app, text="hah", command=checkbox_event(10), variable=check_var,
                                         onvalue="on", offvalue="off")
    checkbox.pack()


    app.mainloop()
    return 0


if __name__ == "__main__":
    main()
