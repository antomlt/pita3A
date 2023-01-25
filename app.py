import cv2 as cv 
import video as vi
import tkinter
import PIL.Image, PIL.ImageTk
import time
import numpy as np

classCascadefacial = cv.CascadeClassifier('cascade.xml')

class App:
    def __init__(self, window, window_title, video_source=0):
         self.window = window
         self.window.title(window_title)
         self.video_source = video_source
         self.vid = vi.Video(self.video_source)
         self.canvas = tkinter.Canvas(window, width = self.vid.width, height = self.vid.height)
         self.canvas.pack()
         if self.vid.x != 0:
            self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
            self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)

         self.btn_snapshot=tkinter.Button(window, text="Snapshot", width=50, command=self.snapshot)
         self.btn_snapshot.pack(anchor=tkinter.CENTER, expand=True)
         self.delay = 15
         self.update()

         self.window.mainloop()

    def snapshot(self):
         ret, frame = self.vid.get_frame(classCascadefacial)
         if ret:
            cv.imwrite("frame-" + time.strftime("%d-%m-%Y-%H-%M-%S") + ".jpg", cv.cvtColor(frame, cv.COLOR_RGB2BGR))

    def update(self):
        ret, frame = self.vid.get_frame(classCascadefacial)
        if ret:
            self.photo = PIL.ImageTk.PhotoImage(image = PIL.Image.fromarray(frame))
            self.canvas.create_image(0, 0, image = self.photo, anchor = tkinter.NW)
 
        self.window.after(self.delay, self.update)
    
