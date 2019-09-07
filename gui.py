import Tkinter
import tkMessageBox
t = Tkinter
tkMB = tkMessageBox
b = Button
p = pack
si = showinfo
se = showerror



top = Tkinter.Tk()
top.title('gui-app')

def helloCallback():
   tkMB.si( "gui-app", "Hello, World!")
   tkMB.si( "gui-app version", "gui-app 2.0, using TkInter")
def badaCallback():
   B3.p()
def notCodedCallback():
   tkMB.se("Sorry", "Not coded yet")
def showMoreCallback():
   B4.p()

B = t.b(top, text ="Hello", command = helloCallback)
B2 = t.b(top, text ="Show more...", command= badaCallback)
B3 = t.b(top, text ="Show even more...", command= showMoreCallback)
B4 = t.b(top, text ="Badaboom!", command=notCodedCallback)


B.p()
B2.p()
tkMB.se("Willkommen!", "Welcome to gui-app")


top.mainloop()
