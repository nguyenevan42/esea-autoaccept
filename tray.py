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

        # Create system tray icon
        self.icon = pystray.Icon("ESEA Autoaccept",
                                title="ESEA Autoaccept",
                                menu=(item("Item1", None)))
        self.image = Image.open(self.path + "\\icon.png")
        self.icon.icon = self.image
        self.icon.run(self.main())

    def main(self):
        self.icon.visible = True
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

    def run(self):
        if __name__ == "__main__":
            Thread(target = self.__init__).start()
    
    def terminate(self):
        sys.exit()

root = App()
root.run()
