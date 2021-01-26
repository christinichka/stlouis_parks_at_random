from tkinter import *
from tkinter import messagebox
import pandas
import random
import csv

BACKGROUND_COLOR = "#006600"
BUTTON_COLOR = "#6699ff"


# # Click Get Park button which generates a random park name from the 
def new_park():
	with open("stl_parks_list.csv") as f:
	  park = f.readlines()
	  chosen_park = random.choice(park)
	  canvas.itemconfig(park_text, text = chosen_park)	


# # Push the "Confirm" button to confirm that you want to visit this park. The park name will then be moved to a new csv of visited parks and removed from the parks list.
def confirm_park():
	park.remove(chosen_park)
	print(len(park))
	data = pandas.DataFrame(park)
	data.to_csv("data/stl_parks_visited.csv", index=False)
	new_park()


# # Push the "Skip" button to skip the park and get a different suggestion. Park names remain on the parks list until they are confirmed.
def skip_park():
	pass


# --- UI Setup ---
window = Tk()
window.title("St. Louis Parks at Random")
window.config(padx=20, pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=300, height=100, bg="white")
park_text = canvas.create_text(
			150, 
			65, 
			text='Ready, set,\n"GET PARK"', 
			width=280,
			fill=BACKGROUND_COLOR,
			font=("Ariel", 20, "italic")
			)
canvas.grid(row=1, column=0, columnspan=2, pady=20, sticky="NESW")
# arch_img = PhotoImage(file="gateway-arch-park.png")
# canvas.create_image(226, 159, image=arch_img)
# canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
# canvas.grid(row=0, column=0, columnspan=2, sticky='')

# --- Label ---
website_label = Label(text="St. Louis Parks at Random", fg="white", bg=BACKGROUND_COLOR)
website_label.grid(column=1, row=0, columnspan=2)

# --- Buttons ---
get_park_button = Button(text="GET PARK", width=20, bg=BUTTON_COLOR, font=("bold"), command=new_park)
get_park_button.grid(column=0, row=2, columnspan=2, sticky='', pady=20) 

confirm_button = Button(text="CONFIRM", width=10, bg=BUTTON_COLOR, font=("bold"), command=confirm_park)
confirm_button.grid(column=0, row=3)

skip_button = Button(text="SKIP", width=10, bg=BUTTON_COLOR, font=("bold"), command=skip_park)
skip_button.grid(column=1, row=3)




# new_park()


window.mainloop()
