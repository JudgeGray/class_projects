"""This is a password generation program written with Python 3.12 and utilizing TKinter and PIL.
The original desing used "splash screens" to create 2 images but there were issues with that. 
Switched to seperate classes for windows and it supported the changes"""

import tkinter as tk
from tkinter import *
import random
import string
from PIL import Image, ImageTk
#Main Window to run the body of the program
class MainWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Password Program")
        master.configure(background = "#8D918D")
        master.geometry("600x400")
        
        #image set in here to allow everything else to overlay it and keep it clean in the GUI
        #coded with try/except due to some issues getting the images to load. This allows the program to 
        #run even if the images are not present/do not load
        #doing the image path like this ensures it runs on anyones pc
        
        image2 = ("genie2.PNG")
        try:
            img2 = Image.open(image2)
            img2 = img2.convert("RGBA")
            photo2 = ImageTk.PhotoImage(img2)    
            image_label2 = Label(master,image = photo2, bg = "#8D918D")
            image_label2.place(relx=.5,rely=.5, anchor = CENTER)
            
            #safeguard incase garbage collection removes the image before it displays
            image_label2.photo2 = photo2
    
        except Exception as e:
            print (f"error loading image2 : {e}")

        #variables have to be initialized before they are called in the methods below
        word_input = Entry(master,borderwidth = 5)
        word_input.place(relx = 0.25, rely = 0.67, anchor = CENTER)
        length_input = Entry(master,borderwidth = 5)
        length_input.place(relx = 0.70, rely = 0.67, anchor = CENTER) 
        
        #labels for main window
        logo = Label(master, bg = "#8D918D" ,text = "Password Genie", font = ("Times New Roman",35))
        logo.place(relx = 0.5,rely = 0.05, anchor = CENTER)        
        word_input_label = Label(master, bg = "#8D918D" ,text = "Make a new password\n from a current password", font = ("Arial",12))
        word_input_label.place(relx = 0.25,rely = 0.58, anchor = CENTER)
        length_input_label = Label(master, bg = "#8D918D" ,text = "Generate a new password\n at your desired length", font = ("Arial",12))
        length_input_label.place(relx = 0.72,rely = 0.58, anchor = CENTER)

        #Method to use in the Exit button    
        def quit_program():
            master.destroy()

        """***Method to randomize input***
        creates a variable called characters that is a list of the letters in word  
        uses random's shuffle feature to rearrange the characters  
        Convert it back into a single string  
        Using Try/Except to prevent null values and errors
        """
        def current_pw():
            try:
                y = word_input.get()
                characters=list(y)
                random.shuffle(characters)
                new_pw= ''.join(characters)
                x=Label(root, text="")
                x.config(text=new_pw)
                x.place(relx = 0.25, rely = 0.74, anchor = CENTER)
            except ValueError:
                x=Label(root, text="")
                x.config(text = "Please enter a length")
                x.place(relx = 0.25, rely = 0.74, anchor = CENTER)
        

        """method to create a password at input length from random numbers and letters
        using string.ascii_letters and string.digits provides a string containing all relevent letters and numbers  
        setting random.choice of all characters to the new string random_pw. Looping for length variable that user input    
        *****point of note for _ in range basically means the loop variable is irrelevent. I don't care about the value in the loop, I just 
        need it to run length times
        Using Try/Except to prevent null values and errors
        """
        def random_pw():
            try:
                y = int(length_input.get()) 
                characters= string.ascii_letters + string.digits
                random_pw = ''.join(random.choice(characters) for _ in range(y))
                x=Label(root, text="")
                x.config(text=random_pw)

                x.place(relx = 0.70, rely = 0.74, anchor = CENTER)
            except ValueError:
                x=Label(root, text="")
                x.config(text = "Please enter a word")
                x.place(relx = 0.70, rely = 0.74, anchor = CENTER)
        
        #These buttons have to be below the methods or else you get an error due to the variables not being defined
        generate1 = Button(root, text = "Generate",padx = 50, pady = 20,bg = "#8D918D", command =current_pw )
        generate1.place(relx = 0.25, rely = 0.86, anchor = CENTER)
        generate2 = Button(root, text = "Generate",padx = 50, pady = 20, bg = "#8D918D", command = random_pw)
        generate2.place(relx = 0.70, rely = 0.86, anchor = CENTER)        
        quit_button = Button(root, text = "EXIT",padx = 20, pady = 15, bg = "#8D918D", command = quit_program)
        quit_button.place(relx = 0.9, rely = 0.9, anchor = CENTER)

    #Method to open the second window
    def open_second_window(self):
        second_window = tk.Toplevel(self.master)
        SecondWindow(second_window)

#Second Window which functions as a splash screen
class SecondWindow:
    def __init__(self, master):
        self.master = master
        self.master.title("Splash Screen")
        master.config(background ="#8D918D")
        master.geometry("300x200")
        
        #same as above image path done like this to ensure it runs on any system
        image_path = ("image1.PNG")
        try:
            img = Image.open(image_path)
            img = img.convert("RGBA")
            photo1 = ImageTk.PhotoImage(img)
            image_canvas = Canvas(master, width=600, height = 400, bg ="#8D918D" )
            image_canvas.pack()
            image_canvas.create_image(0,0,anchor=NW, image=photo1)
    
            image_canvas.photo1 = photo1
   
        except Exception as e:
            print (f"error loading image1 : {e}")
        
        #To make it look more like a program I wanted to create splash screen
        #method to close splash screen and pop the root screen
        def close_splash():
            master.destroy()
            root.deiconify()
        #close splash after 2.5 seconds    
        master.after(2500,close_splash)            

# Create the main Tkinter window
root = tk.Tk()

# Create an instance of the MainWindow class
main_window = MainWindow(root)

# Hide the main window
root.withdraw()

#Create an instance of the second window class
second_window =SecondWindow(tk.Toplevel(root))

# Start the Tkinter event loop
root.mainloop()