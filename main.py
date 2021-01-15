from tkinter import *
from tkinter import messagebox
import pandas
from random import choice
import json

BACKGROUND_COLOR = "#006600"
BUTTON_COLOR = "#6699ff"


# try:
# 	data = pandas.read_csv("stl_parks_visited.csv")
# except FileNotFoundError:
# 	original_data = pandas.read_csv("stl_parks_list.csv")
# 	to_visit = original_data.to_dict(orient="records")
# else:
# 	to_visit = data.to_dict(orient="records")


# def new_park():
# #  	# When the get_park_button is activated this function will pull a random park off of the stl_parks_list.csv and display it to the user.
#  	with open("stl_parks_list.csv") as original_data:
#  		to_visit = original_data.read().split()
#  		current_park = random.choice(to_visit)
# 		# print(current_park)
#  	# canvas.itemconfig(currentark, text=current_park["Park"]


 	

def confirm_park():
	global to_visit
	# Once the random park is selected by the random_park function, the user may confirm the park by clicking the confirm button. The park information will then be deleted off of the stl_parks_list.csv and added to a new document stl_parks_visited.csv
	# The user will see a messagebox pop up telling them the park's name and address.
	# The program will be reset and the entry area will be blank
	to_visit.remove(new_park)
	data = pandas.DataFrame(to_visit)
	data.to_csv("stl_parks_visited.csv", index=False)

def skip_park():
# 	# Once the random park is selected by the random_park function, the user may skip that park by clicking the skip button. The park information will be left where it is and a new random park will be generated and displayed for the user to confirm or skip. 
	new_park()
# 	pass


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
get_park_button = Button(text="GET PARK", width=20, bg=BUTTON_COLOR, font=("bold"))
get_park_button.grid(column=0, row=1, columnspan=2, sticky='', pady=20) 

confirm_button = Button(text="CONFIRM", width=10, bg=BUTTON_COLOR, font=("bold"))
confirm_button.grid(column=0, row=2)

skip_button = Button(text="SKIP", width=10, bg=BUTTON_COLOR, font=("bold"))
skip_button.grid(column=1, row=2)

# --- Entries ---
# park_input = Entry(width=20)
# park_input.grid(column=0, row=2)


# new_park()


window.mainloop()



# Access the stl_parks_list.csv and randomly select one park from the list for the user to visit
# Once selected, remove that park from the list of parks to visit and save it into a new csv file called stl_parks_visited_csv
# Append the stl_parks_list.csv by removing the park from the list so that the next time the user wants to use the app they will get only new parks
# If user wants to skip that park and get a different Park name, skip over that park and leave it in stl_parks_list.csv to be pulled another time.
