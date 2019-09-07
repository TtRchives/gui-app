import Tkinter
import tkMessageBox
t = Tkinter
tkMB = tkMessageBox



top = Tkinter.Tk()
top.title('gui-app')

def helloCallback():
   w.pack
   tkMB.showinfo( "gui-app", "Hello, World!")
def aboutCallback():
   tkMB.showinfo( "gui-app version", "gui-app 2.0, using TkInter")
   tkMB.showinfo( "i am not affiliated with this website!", "thanks to tiny.cc/tkinterguide for providing a guide. other sites:")
   tkMB.showinfo( "not affiliated with this one either", "tiny.cc/tkintertitle (see the one by user8875910) for the title bar")
   tkMB.showinfo( "again, not affiliated", "https://shields.io/ for the README.md badges")
   tkMB.showinfo("not affiliated", "the PSF and Tkinter -- without you this wouldn't exist!")
   tkMB.showinfo("thanks to all of you!", "Thanks so much!")
def badaCallback():
   BSem.pack()
def notCodedCallback():
   tkMB.showerror("Sorry", "Not coded yet")
def showMoreCallback():
   BBada.pack()
def badaCB():
   BAbt.pack()

B = t.Button(top, text ="Hello", command = helloCallback)
BAbt = t.Button(top, text ="About...", command=aboutCallback)
BSm = t.Button(top, text ="Show more...", command= badaCallback)
BSem = t.Button(top, text ="Show even more...", command= showMoreCallback)
BBada = t.Button(top, text ="Badaboom!", command=badaCB)
THello = t.Text ( top, "'Hello' button was pressed")


B.pack()
BSm.pack()
tkMB.showerror("Willkommen!", "Welcome to gui-app")


top.mainloop()
