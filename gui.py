import Tkinter
import tkMessageBox
t = Tkinter
tkMB = tkMessageBox



top = Tkinter.Tk()
top.title('gui-app')

def helloCallback():
   tkMB.showinfo( "gui-app", "Hello, World!")
def aboutCallback():
   tkMB.showinfo( "gui-app version", "gui-app 2.0, using TkInter")
def badaCallback():
   B3.pack()
def notCodedCallback():
   tkMB.showerror("Sorry", "Not coded yet")
def showMoreCallback():
   B4.pack()

B = t.Button(top, text ="Hello", command = helloCallback)
BAbt = t.Button(top, text ="About...", command=aboutCallback)
BSm = t.Button(top, text ="Show more...", command= badaCallback)
BSem = t.Button(top, text ="Show even more...", command= showMoreCallback)
BBada = t.Button(top, text ="Badaboom!", command=notCodedCallback)


B.pack()
B2.pack()
tkMB.showerror("Willkommen!", "Welcome to gui-app")


top.mainloop()
