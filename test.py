import win32com.client, win32gui, os, sys
import pyautogui as pygui
import time
import pystray
from PIL import Image, ImageDraw
from pystray import MenuItem as item, Menu as menu, Icon as icon
import threading
from threading import Thread

class App:
    def __init__(self, *args, **kwargs):
        super(App, self).__init__()
        self.path = os.path.dirname(os.path.realpath(__file__))
        self.main()

    def action(self):
        pass

    def main(self):
        self.img_dir = self.path + "\\data\\" 

        self.rank = ["20yr.png" , "rankd.png", "rankc.png" , "rankb.png" ,
                "ranka.png" , "rankg.png" , "ranks.png" , "dark.png" , "light.png"]
        
        found = False
        while found == False:
            for self.x in range(0,9): 
                if self.click():
                    break

    def click(self):
        try:
            if pygui.locateOnScreen(self.img_dir + self.rank[self.x]): # Check if each image was found
                get_dir = self.img_dir + self.rank[self.x]
                button_coord = pygui.locateOnScreen(get_dir)
                pygui.moveTo(button_coord)
                pygui.click(button_coord, clicks=1)
                print("clicked!")
                return True
            else:
                print("Nothing found.")
        except OSError:
            print(self.rank[self.x], "not found.")
            pass

    def terminate(self):
        sys.exit()

root = App()

def initialize():
        # Create system tray icon
        menu = (item('name', root.action), item('name', root.action))
        print("step1")
        image = Image.open(root.path + "\\icon.png")
        icon = pystray.Icon("ESEA Autoaccept", image,
                                title="ESEA Autoaccept",
                                menu=menu).run()
        print("step2")
        icon.visible = True
        print("step3")
        icon.run(root.App())

initialize()