import Tkinter
import tkMessageBox
t = Tkinter
tkMB = tkMessageBox
from Tkinter import *



top = Tkinter.Tk()
top.title('gui-app')

def helloCallback():
   tkMB.showinfo( "gui-app", "Hello, World!")
   txt1.pack()
def aboutCallback():
   tkMB.showinfo( "gui-app version", "gui-app 2.0, using TkInter")
   tkMB.showinfo( "i am not affiliated with this website!", "thanks to tiny.cc/tkinterguide for providing a guide. other sites:")
   tkMB.showinfo( "not affiliated with this one either", "tiny.cc/tkintertitle (see the one by user8875910) for the title bar")
   tkMB.showinfo( "again, not affiliated", "https://shields.io/ for the README.md badges")
   tkMB.showinfo("dude do you still thing im affiliated with this company?", "https://pythonprogramming.net/tkinter-adding-text-images/")
   tkMB.showinfo("not affiliated", "the PSF and Tkinter -- without you this wouldn't exist!")
   tkMB.showinfo("not affiliated", "https://smallguysit.com/index.php/2017/03/10/tkinter-create-window/, for 'from Tkinter import *'")
   tkMB.showinfo("thanks to all of you!", "Thanks so much!")
def badaCallback():
   BSem.pack()
def notCodedCallback():
   tkMB.showerror("Sorry", "Not coded yet")
def showMoreCallback():
   BBada.pack()
def badaCB():
   BAbt.pack()
#def messageWindow():
    # create child window
    #newWindow = Toplevel()
    # display message
    #message = "This is the child window"
    #Label(win, text=message).pack()
    # quit child window and return to root window
    # the button is optional here, simply use the corner x of the child window
    #Button(win, text='OK', command=win.destroy).pack()

B = t.Button(top, text ="Hello", command = helloCallback)
BAbt = t.Button(top, text ="About...", command=aboutCallback)
BSm = t.Button(top, text ="Show more...", command= badaCallback)
BSem = t.Button(top, text ="Show even more...", command= showMoreCallback)
BBada = t.Button(top, text ="Badaboom!", command=badaCB)
txt1 = Label(top, text="'Hello' button was pressed")
txt2 = Label(top, text="Welcome to gui-app!")

txt2.pack()
B.pack()
BSm.pack()
Button(top, text='Exit', command=top.destroy).pack()
tkMB.showerror("Willkommen!", "Welcome to gui-app")


top.mainloop()
