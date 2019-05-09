from Tkinter import *
import Tkinter as tk
from PIL import ImageTk, Image
import os, random
import datetime

#Create main window
window = tk.Tk()
window.geometry("500x500")


def game():
	#set question counter and score to 0
	global counter
	counter = 0
	global score
	score = 0
	def next(panel):
		global score
		if e1.get().lower() == e2.get():
			#increase score for correct answer
			score += 1
		#display answer
		e1.delete(0)
		e2.configure(state='normal')
		e2.delete(0)
		e2.configure(state='disabled')
		#selects and displays random image
		global letter
		letter = random.choice(os.listdir("./images/"))
		path = "./images/" + letter
		img = ImageTk.PhotoImage(Image.open(path))
		panel.configure(image=img)
		panel.image = img
		#resets next button
		next_button.configure(state="disabled")
		#checks how many questions have been asked
		global counter
		counter += 1
		if counter == 10:
			gameOver()
		

	def show_entry_fields():
		answer = letter.split(".")[0]
		e2.configure(state='normal')
		e2.insert(10, answer)
		e2.configure(state='disabled')
		next_button.configure(state='normal')
	
	#clear menu off of screen
	GameButton.pack_forget()
	ExitButton.pack_forget()
	ScoresButton.pack_forget()
	
	top = tk.Frame(window)
	top.pack(side="top")
	bottom = tk.Frame(window)
	bottom.pack(side="bottom")
	
	#create labels and inputs
	panel = tk.Label(window)
	panel.pack(side = "top", fill = "both", expand = "yes")
	panel2 = tk.Label(window, text="What letter is this?")
	panel2.pack()
	e1 = tk.Entry(window)
	e1.pack()
	panel3 = tk.Label(window, text="The answer is:")
	panel3.pack()
	e2 = tk.Entry(window)
	e2.configure(state="disabled")
	e2.pack()
	
	#place buttons
	show_button = tk.Button(window, text='Show', width=10, height=2, command=show_entry_fields)
	show_button.pack()
	next_button = tk.Button(window, text="Next", width=10, height=2, state="disabled", command=lambda: next(panel))
	next_button.pack(side="right")
	quit_button = tk.Button(window, text='Quit', width=10, height=2, command=window.quit)
	quit_button.pack(side="left")
	
	next(panel)


#main menu
def menu():
    global GameButton
    global ScoresButton
    global ExitButton
    
    GameButton = Button(window, text="New Game", width=15, height=2, command = game)
    GameButton.place(relx=0.5, rely=0.5, anchor=CENTER)

    ScoresButton = Button(window, text="View Previous Scores", width=15, height=2, command = show_scores)
    ScoresButton.place(relx=0.5, rely=0.6, anchor=CENTER)
	
    ExitButton = Button(window, text="Exit", width=10, height=2, command=window.quit)
    ExitButton.pack(side="bottom")

def gameOver():
	def clearButton():
		#clears game over screen
		MenuButton.pack_forget()
		ScoreLabel.place_forget()
		e3.place_forget()
		enterName.place_forget()
		counter = 0
		
	for widget in window.winfo_children():
		widget.destroy()
	#displays score
	global fullscore
	fullscore = str(score) + "/10"
	global ScoreLabel
	ScoreLabel = Label(window, text=fullscore)
	ScoreLabel.place(relx=0.5, rely=0.5, anchor=CENTER)
	global enterName
	enterName = Label(window, text="Enter Name:")
	enterName.place(relx=0.4, rely=0.4, anchor=CENTER)
	global e3
	e3 = tk.Entry(window)
	e3.place(relx=0.6, rely=0.4, anchor=CENTER)
	global MenuButton
	MenuButton = Button(window, text="Back To Menu", width=10, height=2, command =lambda:[menu(),clearButton(),set_score()])
	MenuButton.pack(side="bottom")
	
def set_score():
	file = open("scores.txt", "a")
	filescore = e3.get() + ": " + fullscore + ", " + datetime.datetime.now().strftime("%d-%m-%Y %H:%M") + "\n"
	file.write(filescore)
	file.close()
	
def delete_scores():
	open('scores.txt', 'w').close()
	label.place_forget()
	
def show_scores():
	def clearButton():
		#clears game over screen
		MenuButton.pack_forget()
		label.place_forget()
		DeleteButton.pack_forget()
		
	#clears old menu
	ScoresButton.place_forget()
	GameButton.place_forget()
	ExitButton.pack_forget()
	
	
	#opens scores file
	file = open("scores.txt", "r")
	scores = file.read()
	global label
	label = Label(window, text=scores)
	label.place(relx=0.5, rely=0.5, anchor=CENTER)
	
	global DeleteButton
	DeleteButton = Button(window, text="Clear Scores", width=10, height=2, command = delete_scores)
	DeleteButton.pack(side="top")
	
	
	MenuButton = Button(window, text="Back To Menu", width=10, height=2, command =lambda:[menu(), clearButton()])
	MenuButton.pack(side="bottom")
	
menu()

#Start the GUI
window.mainloop()