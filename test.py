import pystray
import os, sys
from pystray import MenuItem as item, Menu as menu
from PIL import Image, ImageDraw

print("Start")
icon = pystray.Icon('test name')
print("Step 1")

def create_image():
    path = os.path.dirname(os.path.realpath(__file__))
    print("start")
    menu = (item("test", lambda : terminate))
    image = Image.open(path + "\\icon.png")
    icon = pystray.Icon("test", title="ESEA autoaccept", menu=menu)
    print("step1")
    icon.icon = image
    print("step2")
    icon.run(main())
    print("step3")
    return image

def main():
    print("test")
def terminate():
    sys.exit()


icon.icon = create_image()
print("Step 2")
icon.run()
