import tkinter as tk


window = tk.Tk()
window.title('Monster Fight')

label = tk.Label(width=30, height=20, text='Hello world', )
label.pack()
button = tk.Button('Fight')
button.pack()


window.mainloop()