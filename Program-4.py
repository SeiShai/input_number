# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement
# - Created new gitHub repository
# - Upload your programs to gitHub using git bash.
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
input_window.geometry('660x400')
input_window.resizable(0, 0)

# add images
auction_background_data = Image.open("auction_bg.png")
auction_background = CTkImage(dark_image=auction_background_data,
                              light_image=auction_background_data,
                              size=(330, 400))

input_background_data = Image.open("input_bg.png")
input_background = CTkImage(dark_image=input_background_data,
                              light_image=input_background_data,
                              size=(330, 400))

# background
window_frame = CTkFrame(input_window, width=660, height=400)
window_frame.pack()

CTkLabel(window_frame, text="", image=auction_background).pack(expand=True, side="right")
CTkLabel(window_frame, text="", image=input_background).pack(expand=True, side="left")

# titles

# entries
bid_entry1 = CTkEntry(window_frame,
                      width=280,
                      height=35,
                      border_width=1,
                      corner_radius=10,
                      fg_color='#e6e0c8',
                      bg_color='#4A4545',
                      text_color='#000000',
                      placeholder_text='Bidding price 1',
                      placeholder_text_color='#000000',
                      justify=CENTER,
                      font=("times new roman", 20))
bid_entry1.place(relx=0.25, rely=0.35, anchor='center')

bid_entry2 = CTkEntry(window_frame,
                      width=280,
                      height=35,
                      border_width=1,
                      corner_radius=10,
                      fg_color='#e6e0c8',
                      bg_color='#42403D',
                      text_color='#000000',
                      placeholder_text='Bidding price 2',
                      placeholder_text_color='#000000',
                      justify=CENTER,
                      font=("times new roman", 20))
bid_entry2.place(relx=0.25, rely=0.48, anchor='center')

bid_entry3 = CTkEntry(window_frame,
                      width=280,
                      height=35,
                      border_width=1,
                      corner_radius=10,
                      fg_color='#e6e0c8',
                      bg_color='#3D3D39',
                      text_color='#000000',
                      placeholder_text='Bidding price 3',
                      placeholder_text_color='#000000',
                      justify=CENTER, font=("times new roman", 20))
bid_entry3.place(relx=0.25, rely=0.61, anchor='center')

# buttons
Confirm_button = CTkButton(window_frame,
                         text="Confirm",
                         fg_color="#1e8881",
                         hover_color="#E44982",
                         font=("Arial Bold", 12),
                         text_color="#ffffff",
                         width=280,
                         height=35)
Confirm_button.place(relx=0.25, rely=0.80, anchor='center')




input_window.mainloop()