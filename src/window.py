from tkinter import *
import tkinter
class window(tkinter.Tk):
    def __init__(self,*args,**kwargs):
        tkinter.Tk.__init__(self,*args,**kwargs)
        # Adding a title
        self.wm_title("Calculator")