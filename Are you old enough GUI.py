
# When both values have been entered, check if the person
# is the right age to go on an 18-30 holiday (they must be over 18 and under 31).
# If they are, welcome them to the holiday, otherwise print a (polite) message refusing them entry.

from tkinter import * #imports the entire tkinter library
from tkinter import messagebox

root = Tk() #blank window called 'root'
root.title("Age range validator")
root.geometry("500x350+0+0")

heading = Label(root, text="Lets see if you are the right age!", font=("arial", 15, "bold"), fg="red").pack() #creates a label of text
label_name = Label(root, text="Please enter your name:", font=("arial", 20, "bold"), fg="green").place(x=10, y=100)
label_age = Label(root, text="Please enter your age:", font=("arial", 20, "bold"), fg="green").place(x=10, y=200)


nameEntry_box = Entry(root, width=25, bg="white")
nameEntry_box.place(x=340, y=111)

ageEntry_box = Entry(root, width=25, bg="white")
ageEntry_box.place(x=340, y=210)


def check_age():

    if (int(ageEntry_box.get() or 0) >=18) and (int(ageEntry_box.get() or 0) <=30):
        messagebox.showinfo("Congrats!", "Welcome to the holiday trip for people between the ages of 18 and 30, "
                + nameEntry_box.get() +"!" + " Sorta weird, eh?")
    else:
        messagebox.showinfo("Error", "Sorry "
                + nameEntry_box.get() + ", you are not within the age range to go on this trip")

check = Button(root, text="Check Now", width=30, height=5, bg="white", command= check_age).place(x=120, y=250)

root.mainloop() #mainloop creates an inf loop of the open window so it stays open





