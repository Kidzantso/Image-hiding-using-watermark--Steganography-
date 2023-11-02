# Python program to create 
# a file explorer in Tkinter

# import all components
# from the tkinter library
from tkinter import *
import cv2
import sys
import os 
# import filedialog module
from tkinter import filedialog
# Function for opening the 
# file explorer window

def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("images","*.jpg*"),("images","*.png*"),("images","*.jpeg*")))
	
	# Change label contents
	label_file_explorer1.configure(text=filename)

def browseFiles2():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("images","*.jpg*"),("images","*.png*"),("images","*.jpeg*")))
	
	# Change label contents
	label_file_explorer2.configure(text=filename)
  																								
def encrypt():
	if(label_file_explorer1.cget("text")=="image 1" or label_file_explorer2.cget("text")=="image 2" or label_file_explorer1.cget("text")=="" or label_file_explorer2.cget("text")==""):
		label_file_explorer3.configure(text="You didn't select the 2 images")
	elif(label_file_explorer1.cget("text")==label_file_explorer2.cget("text")):
		label_file_explorer3.configure(text="You have chosen the same image or same size images")
	else:
		directory=filedialog.askdirectory()
	# Change label contents
		os.chdir(directory)
	# img1 and img2 are the
	# two input images
		img1 = cv2.imread(label_file_explorer1.cget("text"))
		img2 = cv2.imread(label_file_explorer2.cget("text"))
		height1, width1 = img1.shape[:2]
		height2, width2 = img2.shape[:2]
		if(width1>width2 and height1>height2):
			for i in range(img2.shape[0]):
				for j in range(img2.shape[1]):
					for l in range(3):

				# v1 and v2 are 8-bit pixel values
				# of img1 and img2 respectively
						v1 = format(img1[i][j][l], '08b')
						v2 = format(img2[i][j][l], '08b')

				# Taking 4 MSBs of each image
						v3 = v1[:4] + v2[:4]

						img1[i][j][l]= int(v3, 2)

			label_file_explorer3.configure(text="File saved")
			cv2.imwrite("encryptedimg.png", img1)
		else:
			label_file_explorer3.configure(text="Chosen image to hide is larger than first image")
# Create the root window
window = Tk()

# Set window title
window.title('Images encryption')

# Set window size
window.geometry("700x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer1 = Label(window, text = "image 1",width = 100, height = 4, fg = "blue")
label_file_explorer2 = Label(window, text = "image 2",width = 100, height = 4, fg = "blue")
label_file_explorer3 = Label(window, text = "save to",width = 100, height = 4, fg = "blue")
	
button_explore1 = Button(window, text = "Choose first image",command = browseFiles) 
button_explore2 = Button(window, text = "Choose second image",command = browseFiles2)
button_save = Button(window, text = "encrypt and save",command = encrypt) 

button_exit = Button(window, text = "Exit",command = sys.exit) 

# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer1.grid(column = 1, row = 1)
label_file_explorer2.grid(column = 1, row = 2)
label_file_explorer3.grid(column = 1, row = 3)

button_explore1.grid(column = 1, row = 4)
button_explore2.grid(column = 1, row = 5)
button_save.grid(column = 1, row = 6)

button_exit.grid(column = 1,row = 8)

# Let the window wait for any events
window.mainloop()
