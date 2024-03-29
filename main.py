from tkinter import *
from tkinter import messagebox
import pandas
import random
import csv

BACKGROUND_COLOR = "#006600"
BUTTON_COLOR = "#6699ff"


with open("stl_parks_list.csv") as f:
	park = f.read().splitlines()

def new_park():
	global chosen_park
	chosen_park = random.choice(park)
	canvas.itemconfig(park_text, text=chosen_park)

def confirm_park():
	park.remove(chosen_park)
	print(len(park))
	with open("stl_parks_visited.csv", "a") as f:
		print(chosen_park, file=f)


# --- UI Setup ---
window = Tk()
window.title("St. Louis Parks at Random")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=300, height=250, bg="white")

arch_img = PhotoImage(file="gateway-arch-park.png")
canvas.create_image(150, 70, image=arch_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=1, column=0, columnspan=4, sticky='')

park_text = canvas.create_text(
			150, 
			210, 
			width=280,
			fill="white",
			font=("Ariel", 20, "italic")
			)
canvas.grid(row=3, column=0, columnspan=4, pady=20, sticky="NESW")


# --- Label ---
website_label = Label(
	text="St. Louis Parks at Random", 
	fg="white", 
	bg=BACKGROUND_COLOR,
	font=("Ariel", 11, "italic")
	)
website_label.grid(column=2, row=0, columnspan=2)


# --- Buttons ---

# "Get Park" button generates a random park name from the stl_parks_list.csv
# get_park_button = Button(text="GET PARK", width=20, bg=BUTTON_COLOR, font=("bold"), command=new_park)
# get_park_button.grid(column=0, row=2, columnspan=2, sticky='', pady=20) 

# "Confirm" button cornfirms that you want to visit this park. The park name will then be moved to a new csv of stl_visited_parks.csv and removed from the stl_parks_list.csv.
confirm_button = Button(
	text="CONFIRM", 
	width=10, 
	bg=BUTTON_COLOR, 
	font=("bold"), 
	command=confirm_park)
confirm_button.grid(column=1, row=4)

# Push the "Skip" button to skip the park and get a different suggestion. Park names remain on the parks list until they are confirmed.
skip_button = Button(
	text="SKIP", 
	width=10, 
	bg=BUTTON_COLOR, 
	font=("bold"), 
	command=new_park)
skip_button.grid(column=3, row=4)



new_park()


window.mainloop()
