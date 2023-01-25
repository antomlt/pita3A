import cv2 as cv 
import video as vi
import app as a
import facialdetection as f1
import image_recognition.window_detection_live as wdl
import tkinter
import PIL.Image, PIL.ImageTk
import time
import numpy as np

classCascadefacial = cv.CascadeClassifier('cascade.xml')
my_app = a.App(tkinter.Tk(), "Tkinter and OpenCV")
my_app.mainloop()









