import Tkinter
import tkMessageBox
t = Tkinter
tkMB = tkMessageBox



top = Tkinter.Tk()
top.title('gui-app')

def helloCallback():
   tkMB.showinfo( "gui-app", "Hello, World!")
def badaCallback():
   B3.pack()
def notCodedCallback():
   tkMB.showerror("Sorry", "Not coded yet")
def showMoreCallback():
   B4.pack()

B = t.Button(top, text ="Hello", command = helloCallback)
B2 = t.Button(top, text ="Show more...", command= badaCallback)
B3 = t.Button(top, text ="Show even more...", command= showMoreCallback)
B4 = t.Button(top, text ="Badaboom!", command=notCodedCallback)


B.pack()
B2.pack()
tkMB.showerror("Willkommen!", "Welcome to gui-app")


top.mainloop()
