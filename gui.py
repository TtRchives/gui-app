import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)


tkMessageBox.showerror("Willkommen!", "Welcome to slate alpha")


B.pack()
top.mainloop()
