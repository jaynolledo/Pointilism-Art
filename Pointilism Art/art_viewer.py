"""

This program will provide a function that opens a specified text file,
and draws the pointillist art in a graphical window.This will involve
reading from a text file that was created by art_maker.py and using
each line of the file to place a colored circle in the graphics window.


"""
from graphics import *
import tkinter as tk
from tkinter import filedialog

WINDOW_SIZE = 600

def display(artFileName):
    if artFileName[-3:] == 'art':
        fin = open(artFileName, 'r')
        imageSize = fin.readline()
        imageSize = int(imageSize)
        window = GraphWin("Art Viewer", WINDOW_SIZE, WINDOW_SIZE)
        window.setBackground('black')
        scale = imageSize / WINDOW_SIZE
        for line in fin:
            numList = line.split()
            x = int(numList[0]) / scale
            y = int(numList[1]) / scale
            radius = int(numList[2])
            r = int(numList[3])
            g = int(numList[4])
            b = int(numList[5])
            circle = Circle(Point(x, y), radius)
            color = color_rgb(r, g, b)
            circle.setFill(color)
            circle.setOutline(color)
            circle.draw(window)
        fin.close()
        
    else:
        print("Invalid file format. Must choose an 'art' file. Ending execution.")
        exit(-1)

def main():
    # opens a file dialog to choose a file
    root = tk.Tk()
    root.withdraw()
    file_path = filedialog.askopenfilename()
    print(file_path)
    display(file_path)

main()