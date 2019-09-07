import Tkinter
import tkMessageBox


root = tkinter.Tk()
root.title('My Title')

top = Tkinter.Tk()

def helloCallBack():
   tkMessageBox.showinfo( "gui-app", "Hello, World!")
def badaCallback():
   B3.pack()
def showMoreCallback():
   tkMessageBox.showerror("Sorry", "Not coded yet")

B = Tkinter.Button(top, text ="Hello", command = helloCallback)
B2 = Tkinter.Button(top, text ="Badaboom!", command= badaCallback)
B3 = Tkinter.Button(top, text ="Show More...", command= showMoreCallback)


tkMessageBox.showerror("Willkommen!", "Welcome to gui-app")


B.pack()
B2.pack()
top.mainloop()
