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
   #tkMB.showinfo( "gui-app version", "gui-app 2.0, using TkInter")
   #tkMB.showinfo( "i am not affiliated with this website!", "thanks to tiny.cc/tkinterguide for providing a guide. other sites:")
   #tkMB.showinfo( "not affiliated with this one either", "tiny.cc/tkintertitle (see the one by user8875910) for the title bar")
   #tkMB.showinfo( "again, not affiliated", "https://shields.io/ for the README.md badges")
   #tkMB.showinfo("dude do you still thing im affiliated with this company?", "https://pythonprogramming.net/tkinter-adding-text-images/")
   #tkMB.showinfo("not affiliated", "the PSF and Tkinter -- without you this wouldn't exist!")
   #tkMB.showinfo("not affiliated", "https://smallguysit.com/index.php/2017/03/10/tkinter-create-window/, for 'from Tkinter import *'")
   #tkMB.showinfo("thanks to all of you!", "Thanks so much!")
   #create child window
   about = Toplevel()
   about.title("About gui-app")
   #display message
   Label(about, text="gui-app 2.1 build 6").pack()
   Label(about).pack()
   Label(about, text="CREDITS: (NOT AFFILIATED WITH ANY OF THESE SITES)").pack()
   Label(about).pack()
   Label(about, text="Thanks to tiny.cc/tkinterguide for providing a guide.").pack
   Label(about, text="Thanks to tiny.cc/tkintertitle (see the one by user8875910) for the title bar").pack()
   Label(about, text="Thanks also to shields.io for the README.md badges").pack()
   Label(about, text="Thanks also to pythonprogramming.net/tkinter-adding-text-images/ for a nice article (can't remember what it taught me though)").pack()
   Label(about, text="Thanks so much to the Python Software Foundation and TkInter -- without you this wouldn't exist!").pack()
   Label(about, text="Thanks to smallguysit.com/index.php/2017/03/10/tkinter-create-window/ for 'from Tkinter import *'").pack()
   Label(about, text="Thanks to tiny.cc/childwindow for the guide on child windows -- it helped with this window!").pack()
   Label(about).pack()
   Label(about, text="Thanks to all!").pack()
   #quit child window and return to root window
   #the button is optional here, simply use the corner x of the child window
   Button(about, text='OK', command=about.destroy).pack()
def badaCallback():
   BSem.pack()
def notCodedCallback():
   tkMB.showerror("Sorry", "Not coded yet")
def showMoreCallback():
   BBada.pack()
def badaCB():
   BAbt.pack()
   Button(top, text='Exit', command=top.destroy).pack()
   Button(top, command=easterEggCallback).pack()
def messageWindow():
    #create child window
    newWindow = Toplevel()
    #display message
    message = "This is the child window"
    Label(newWindow, text=message).pack()
    #quit child window and return to root window
    #the button is optional here, simply use the corner x of the child window
    Button(newWindow, text='OK', command=newWindow.destroy).pack()
def easterEggCallback():
  txt3.pack()
def menuCB():
   

B = t.Button(top, text ="Hello", command = helloCallback)
BAbt = t.Button(top, text ="About...", command=aboutCallback)
BSm = t.Button(top, text ="Show more...", command= badaCallback)
BSem = t.Button(top, text ="Show even more...", command= showMoreCallback)
BBada = t.Button(top, text ="Badaboom!", command=badaCB)
BMenu = t.Button(top, text="Show menubar", command=menuCB).pack()

txt1 = Label(top, text="'Hello' button was pressed")
txt2 = Label(top, text="Welcome to gui-app!")
txt3 = Label(top, text="NOTE: You pressed the Easter egg!")

txt2.pack()
B.pack()
BSm.pack()
tkMB.showerror("Willkommen!", "Welcome to gui-app")


top.mainloop()
