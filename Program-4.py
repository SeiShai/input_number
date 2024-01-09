# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement
# - Created new github repository
# - Upload your programs to github using git bash.
# - Record a demo presenting your programs (less than 2 min only)
# - Send the demo directly to my messenger
# - Deadline before Jan 13, 2024

# import packages
import customtkinter
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image

# set theme
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

# create window
input_window = ctk.CTk()
input_window.title("Ship Shop")
input_window.geometry('350x400')
input_window.resizable(0, 0)

# add images
auction_background_data = Image.open("auction_bg.png")
auction_background = CTkImage(dark_image=auction_background_data,
                              light_image=auction_background_data,
                              size=(350, 400))

# background
window_frame = CTkFrame(input_window, width=700, height=400)
window_frame.pack()

window_label = CTkLabel(window_frame, text='', image=auction_background, width=350, height=400)
window_label.pack(fill='both', expand=True)

# entries




input_window.mainloop()