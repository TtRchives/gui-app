import Tkinter
import tkMessageBox

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "Hello Python", "Hello World")

B = Tkinter.Button(top, text ="Hello", command = helloCallBack)
B2 = Tkinter.Button(top, text ="Badaboom!", command= helloCallBack)


tkMessageBox.showerror("Willkommen!", "Welcome to gui-app")


B.pack()
B2.pack()
top.mainloop()
