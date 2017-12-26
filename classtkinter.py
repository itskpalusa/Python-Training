# classes with tkinter

from tkinter import *

class Application(Frame):
    """A simple GUI application"""

    def __init__(self, master):
        """Inititalize the frame"""
        Frame.__init__(self,master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
      self.button = Button(self, text = "Button1")
      self.button1.grid()

root =Tk()
root.title("class buttons")
root.geometry("200x90")

app = Application(root)
root.mainloop()
