import tkinter as tk
from tkinter import *
root = Tk()
root.title("Monster Fight")
photo = PhotoImage(file="spider2.png")
Button(root, image=photo).pack()
ATKButton = Button(root, text="Attack")
ATKButton.pack()
HEALButton = Button(root, text="HEAL")
HEALButton.pack()
root.mainloop()
