
# Access the stl_parks_list.csv and randomly select one park from the list for the user to visit
# Once selected, remove that park from the list of parks to visit and save it into a new csv file called stl_parks_visited_csv
# Append the stl_parks_list.csv by removing the park from the list so that the next time the user wants to use the app they will get only new parks
# If user wants to skip that park and get a different Park name, skip over that park and leave it in stl_parks_list.csv to be pulled another time.

from tkinter import *
import pandas
from random import choice, randint, shuffle

BACKGROUND_COLOR = "#006600"

def random_park():

def confirm_park():

def skip_park():
	

# data = pandas.read_csv("stl_parks_list")


# --- UI Setup ---
window = Tk()
window.title("St. Louis Parks at Random")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=500, height=400)
arch_img = PhotoImage(file="gateway-arch-park.png")
canvas.create_image(324, 228, image=arch_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, )



# --- Buttons ---

get_park_button = Button(text="Get Park", width=15)
get_park_button.grid(column=1, row=1) 

confirm_button = Button(text="Confirm Park Choice", width=15)
confirm_button.grid(column=0, row=2)

skip_button = Button(text="Skip", width=15)
skip_button.grid(column=1, row=2)

# --- Entries ---

park_input = Entry(width=50)
park_input.grid(column=0, row=1)

window.mainloop()