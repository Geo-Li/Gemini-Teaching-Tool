from customtkinter import *

# Set appearance and color theme
set_appearance_mode("System")  # 'light', 'dark', or 'System'
set_default_color_theme("blue")  # Blue theme

app = CTk()
app.geometry("600x200")  # Adjust size as needed
app.title("CustomTkinter Layout")

# Configure the grid layout manager
app.grid_columnconfigure(0, weight=1)  # This column will contain the first row widgets
app.grid_columnconfigure(1, weight=2)  # This column will contain the entry

app.grid_rowconfigure(0, weight=1)  # First row (label and entry)
app.grid_rowconfigure(1, weight=1)  # Second row (buttons)

# Create Label in row 1, column 1
label = CTkLabel(app, text="Enter something:")
label.grid(row=0, column=0, sticky="ew")  # 'ew' stretches the widget east-west

# Create Entry in row 1, column 2
entry = CTkEntry(app)
entry.grid(row=0, column=1, sticky="ew")

# Button frame for better control over button widths
button_frame = CTkFrame(app)
button_frame.grid(row=1, column=0, columnspan=2, sticky="ew")
button_frame.grid_columnconfigure(0, weight=1)
button_frame.grid_columnconfigure(1, weight=1)

# Create Button1 in button frame
button1 = CTkButton(button_frame, text="Button 1")
button1.grid(row=0, column=0, sticky="ew")

# Create Button2 in button frame
button2 = CTkButton(button_frame, text="Button 2")
button2.grid(row=0, column=1, sticky="ew")

app.mainloop()
