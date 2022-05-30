"""

This program uses a function to convert square GIF images into a specific
text file format that describes the placement of many colored circles that
is a “pointillist” version of that image.

"""
from graphics import *
import random
import tkinter as tk
from tkinter import filedialog

NUM_CIRCLES = 5000

def convert(imageFileName):
        if 'gif' in imageFileName:
            image = Image(Point(0, 0), imageFileName)
            outFile = imageFileName.replace('gif', 'art')
            fout = open(outFile, 'w')
            imageSize = image.getWidth()
            fout.write(f'{imageSize}\n')
            for i in range(NUM_CIRCLES):
                x = random.randrange(imageSize)
                y = random.randrange(imageSize)
                radius = random.randrange(2, 9)
                color = image.getPixel(x,y)
                r = color[0]
                g = color[1]
                b = color[2]
                fout.write(f'{x} {y} {radius} {r} {g} {b}\n')
                
            fout.close()
            
        else:
            print("Invalid file format. Must choose a 'gif' file. Ending execution")
            exit(-1)
                
def main():
    # opens file dialog to choose a file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    convert(file_path)

main()
