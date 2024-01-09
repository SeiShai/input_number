# Ask user to input 3 numbers. Find and print the biggest number using only if-else statement
# - Created new gitHub repository
# - Upload your programs to gitHub using git bash.
# - Record a demo presenting your programs (less than 2 min only)
# - Send the demo directly to my messenger
# - Deadline before Jan 13, 2024

# import modules
import customtkinter
import customtkinter as ctk
from tkinter import *
from tkinter import messagebox
from customtkinter import *
from PIL import Image

# def
def confirm():

    bid1 = bid_entry1.get()
    bid2 = bid_entry2.get()
    bid3 = bid_entry3.get()

    # check if empty or digits
    if any(not entry for entry in (bid1, bid2, bid3)):
        messagebox.showwarning('Invalid', 'Please enter a valid amount')
        return

    if not (bid1.isdigit() and bid2.isdigit() and bid3.isdigit()):
        messagebox.showerror('Invalid', 'Please enter a valid amount')
        return

    # Convert bids to integers
    bid1 = int(bid1)
    bid2 = int(bid2)
    bid3 = int(bid3)

    # Check if bids are more than 100,000
    if bid1 <= 100000 or bid2 <= 100000 or bid3 <= 100000:
        messagebox.showwarning('Invalid', 'Bids should be more than 100,000')
        return

    if bid1 >= bid2 and bid1 >= bid3:
        largest = bid1
    elif bid2 >= bid1 and bid2 >= bid3:
        largest = bid2
    else:
        largest = bid3

    if bid1 and bid2 and bid3:
        input_window.destroy()

        # results window
        results_window = ctk.CTk()
        results_window.title('Congratulations')
        results_window.geometry('600x300')
        results_window.resizable(0, 0)

        # add bg image
        results_background_data = Image.open("results_bg.png")
        results_background = CTkImage(dark_image=results_background_data,
                                      light_image=results_background_data,
                                      size=(600, 300))

        # add widgets
        results_frame = CTkFrame(results_window, width=600, height=300)
        results_frame.pack()

        CTkLabel(results_frame, text="", image=results_background).pack(expand=True)

        formatted_largest = "{:,}".format(largest)
        results_label = CTkLabel(results_frame, text=f"For being the highest bidder with:\n\n"
                                                     f"$ {formatted_largest}",
                                 fg_color='transparent',
                                 bg_color='transparent',
                                 font=("Lucida fax", 30))
        results_label.place(relx=0.5, rely=0.6, anchor='center')

        results_window.mainloop()


# create window
input_window = ctk.CTk()
input_window.title("Auctions")
input_window.geometry('660x400')
input_window.resizable(0, 0)

# set theme
customtkinter.set_appearance_mode('dark')
customtkinter.set_default_color_theme('green')

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
                      font=("lucida fax", 20))
bid_entry1.place(relx=0.25, rely=0.37, anchor='center')

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
                      font=("lucida fax", 20))
bid_entry2.place(relx=0.25, rely=0.50, anchor='center')

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
                      justify=CENTER, font=("lucida fax", 20))
bid_entry3.place(relx=0.25, rely=0.63, anchor='center')

# buttons
Confirm_button = CTkButton(window_frame,
                         command=confirm,
                         text="Confirm",
                         fg_color="#1e8881",
                         hover_color="#E44982",
                         font=("Arial Bold", 12),
                         text_color="#ffffff",
                         width=280,
                         height=35)
Confirm_button.place(relx=0.25, rely=0.83, anchor='center')

input_window.mainloop()
