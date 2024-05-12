'''
Scoreboard
By Michael Boylan
A program used to keep track of the score of a basketball game by adding 1, 2, or 3 points to the score for the respective team

05.12.24
'''
from tkinter import Tk, Button, StringVar, Label, Entry

# Create the main window
root = Tk()
root.title("Scoreboard")
root.geometry("500x400")

# Function to get team names from user input
def get_team_names():
  global team_a_name, team_b_name
  team_a_name = entry_a.get()
  team_b_name = entry_b.get()
  # Update team labels with entered names
  team_a_label.config(text=team_a_name)
  team_b_label.config(text=team_b_name)
  # Hide the entry fields and button after getting names
  entry_a.grid_remove()
  entry_b.grid_remove()
  button_get_names.grid_remove()

# Initialize score variables
team_a_score = StringVar()
team_a_score.set("0")
team_b_score = StringVar()
team_b_score.set("0")

# Initially set team names to empty strings (before user input)
team_a_name = ""
team_b_name = ""

# Updates score for selected team
def update_score(team, amount):
  current_score = int(team_a_score.get() if team == "team_a" else team_b_score.get())
  new_score = current_score + amount
  if team == "team_a":
    team_a_score.set(str(new_score))
  else:
    team_b_score.set(str(new_score))

# Create entry fields and button to get team names
entry_a = Entry(root, width=15)
entry_a.grid(row=0, column=1)
entry_b = Entry(root, width=15)
entry_b.grid(row=1, column=1)
button_get_names = Button(root, text="Enter Team Names", command=get_team_names)
button_get_names.grid(row=2, column=1)

# Create labels for Team A and Team B (initially without names)
team_a_label = Label(root, text="Home Team:", font=("Arial", 20))
team_a_label.grid(row=0, column=0, pady=20)  # Added padding to move label above score

team_b_label = Label(root, text="Away Team:", font=("Arial", 20))
team_b_label.grid(row=1, column=2, pady=20)  # Added padding to move label above score

# Create score displays using the score variables and a larger font
team_a_display = Label(root, textvariable=team_a_score, font=("Arial", 50))
team_a_display.grid(row=2, column=0)  # Moved score display down below label

team_b_display = Label(root, textvariable=team_b_score, font=("Arial", 50))
team_b_display.grid(row=2, column=2)  # Moved score display down below label

# Create buttons for 1, 2, and 3 points
button_a_3 = Button(root, text="+3", command=lambda: update_score("team_a", 3), font=("Arial", 15))
button_a_3.grid(row=4, column=0)
button_a_2 = Button(root, text="+2", command=lambda: update_score("team_a", 2), font=("Arial", 15))
button_a_2.grid(row=5, column=0)
button_a_1 = Button(root, text="+1", command=lambda: update_score("team_a", 1), font=("Arial", 15))
button_a_1.grid(row=6, column=0)

button_b_3 = Button(root, text="+3", command=lambda: update_score("team_b", 3), font=("Arial", 15))
button_b_3.grid(row=4, column=2)
button_b_2 = Button(root, text="+2", command=lambda: update_score("team_b", 2), font=("Arial", 15))
button_b_2.grid(row=5, column=2)
button_b_1 = Button(root, text="+1", command=lambda: update_score("team_b", 2), font=("Arial", 15))
button_b_1.grid(row=6, column=2)

# Opens pop up window
root.mainloop()