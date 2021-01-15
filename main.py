from tkinter import *
from tkinter import messagebox
import pandas
import random
import json

BACKGROUND_COLOR = "#006600"
BUTTON_COLOR = "#6699ff"

current_park = {}
to_visit = {}

# try:
# 	data = pandas.read_csv("stl_parks_visited.csv")
# except FileNotFoundError:
# 	original_data = pandas.read_csv("stl_parks_list.csv")
# 	to_visit = original_data.to_dict(orient="records")
# else:
# 	to_visit = data.to_dict(orient="records")

# Push "Get Park" button to get the name of a random park to visit
def new_park():

	current_park = park_input.get()
	new_data = {
		park: {"Park": park}
	}
	 	with open("stl_parks_list.csv") as original_data:
	 		to_visit = original_data.read().split()
	 		current_park = random.choice(to_visit)
	 		messagebox.showinfo(title=current_park, message=f"Your park is: {to_visit}")
		# print(current_park)}
	 		

# Push the "Confirm" button to confirm that you want to visit this park. The park name will then be moved to a new csv of visited parks and removed from the parks list.
def confirm_park():
	to_visit.remove(current_park)
	print(len(to_visit))
	data = pandas.DataFrame(to_visit)
	data.to_csv("stl_parks_visited.csv", index=False)
	# messagebox.showinfo(title=current_park, message=f"Your park is: {current_park}")
	pass

# Push the "Skip" button to skip the park and get a different suggestion. Park names remain on the parks list until they are confirmed.
def skip_park(): 
	pass


# --- UI Setup ---
window = Tk()
window.title("St. Louis Parks at Random")
window.config(pady=20, bg=BACKGROUND_COLOR)

canvas = Canvas(width=400, height=300)
arch_img = PhotoImage(file="gateway-arch-park.png")
canvas.create_image(226, 159, image=arch_img)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
canvas.grid(row=0, column=0, columnspan=2, sticky='')

# --- Label ---
website_label = Label(text="St. Louis Parks at Random")
website_label.grid(column=0, row=0, columnspan=2)

# --- Buttons ---
get_park_button = Button(text="GET PARK", width=20, bg=BUTTON_COLOR, font=("bold"), command=new_park)
get_park_button.grid(column=0, row=2, columnspan=2, sticky='', pady=20) 

confirm_button = Button(text="CONFIRM", width=10, bg=BUTTON_COLOR, font=("bold"), command=confirm_park)
confirm_button.grid(column=0, row=3)

skip_button = Button(text="SKIP", width=10, bg=BUTTON_COLOR, font=("bold"), command=skip_park)
skip_button.grid(column=1, row=3)

# --- Entries ---
park_input = Entry(width=20)
park_input.grid(column=0, row=1, columnspan=2)


# new_park()


window.mainloop()
