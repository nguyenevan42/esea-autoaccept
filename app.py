import tkinter as tk
from tkinter import Tk, Label, Button, DISABLED, NORMAL
import win32com.client, win32gui, os
import pyautogui as pygui
import time

class App(tk.Frame):
    def __init__(self, *args, **kwargs):
        super(App, self).__init__()
        self.label1 = tk.Label()
        self.button0 = tk.Button(text="Refresh", command=self.refresh)
        self.button1 = tk.Button(text="Start", command=self.main)
        self.label1.pack()
        self.button0.pack()
        self.button1.pack()
        self.app_check()
        
    def app_check(self):
        if win32gui.FindWindow(None, "ESEA Client"):
            self.button1["state"] = NORMAL
            self.label1["text"] = "ESEA is running"
        else:
            self.button1["state"] = DISABLED
            self.label1["text"] = "ESEA is not running"

    def main(self):
        self.img_dir = os.path.dirname(os.path.realpath(__file__)) + "\\data\\" 

        self.rank = ["20yr.png" , "rankd.png", "rankc.png" , "rankb.png" ,
                 "ranka.png" , "rankg.png" , "ranks.png" , "dark.png" , "light.png"]
        
        found = False
        while found == False:
            for self.x in range(0,9): 
                if self.click():
                    break
            
    def click(self):
        #print("img", self.x)
        try:
            if pygui.locateOnScreen(self.img_dir + self.rank[self.x]): #check if each image was found
                get_dir = self.img_dir + self.rank[self.x]
                button_coord = pygui.locateOnScreen(get_dir)
                pygui.moveTo(button_coord)
                pygui.click(button_coord, clicks=1)
                print("clicked!")
                return True
            else:
                print("Nothing found.")
                time.sleep(2)
        except OSError:
            print(self.rank[self.x], "not found.")
            pass

    def refresh(self):
        self.app_check()

if __name__ == "__main__":
    root = Tk()
    root.title("test")
    root.iconbitmap(os.path.dirname(os.path.realpath(__file__)) + "\\icon.ico")
    root.geometry("200x75")
    app = App(root)
    root.mainloop()
