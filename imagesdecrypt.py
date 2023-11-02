# Python program

# import all components
# from the tkinter library
import sys
from tkinter import *
import cv2
import numpy as np
import random
import os 
# import filedialog module
from tkinter import filedialog
from tkinter.filedialog import asksaveasfile
# Function for opening the 
# file explorer window

def browseFiles():
	filename = filedialog.askopenfilename(initialdir = "/",title = "Select a File",filetypes = (("images","*.jpg*"),("images","*.png*"),("images","*.jpeg*")))
	
	# Change label contents
	label_file_explorer1.configure(text=filename)
																							
def decrypt():
	if(label_file_explorer1.cget("text")=="image"or label_file_explorer1.cget("text") == ""):
		label_file_explorer3.configure(text="You didn't select the image")
	else:
		directory=filedialog.askdirectory()
		if(directory!=''):
			label_file_explorer3.configure(text="File saved")
			os.chdir(directory)
			img = cv2.imread(label_file_explorer1.cget("text"))
			width = img.shape[0]
			height = img.shape[1]

		# img1 and img2 are two blank images
			img1 = np.zeros((width, height, 3), np.uint8)
			img2 = np.zeros((width, height, 3), np.uint8)

			for i in range(width):
				for j in range(height):
					for l in range(3):
						v1 = format(img[i][j][l], '08b')
						v2 = v1[:4] + chr(random.randint(0, 1)+48) * 4
						v3 = v1[4:] + chr(random.randint(0, 1)+48) * 4

					# Appending data to img1 and img2
						img1[i][j][l]= int(v2, 2)
						img2[i][j][l]= int(v3, 2)

	# These are two images produced from
	# the encrypted image
			cv2.imwrite("original_img_1.png", img1)
			cv2.imwrite("original_img_2.png",img2)

# Create the root window
window = Tk()

# Set window title
window.title('Images decryption')

# Set window size
window.geometry("700x500")

#Set window background color
window.config(background = "white")

# Create a File Explorer label
label_file_explorer1 = Label(window, text = "image",width = 100, height = 4, fg = "blue")
label_file_explorer3 = Label(window, text = "save to",width = 100, height = 4, fg = "blue")
	
button_explore1 = Button(window, text = "Choose your image",command = browseFiles) 
button_save = Button(window, text = "decrypt and save",command = decrypt) 

button_exit = Button(window, text = "Exit",command = sys.exit) 

# Grid method is chosen for placing
# the widgets at respective positions 
# in a table like structure by
# specifying rows and columns
label_file_explorer1.grid(column = 1, row = 1)
label_file_explorer3.grid(column = 1, row = 3)

button_explore1.grid(column = 1, row = 4)
button_save.grid(column = 1, row = 6)

button_exit.grid(column = 1,row = 8)

# Let the window wait for any events
window.mainloop()
