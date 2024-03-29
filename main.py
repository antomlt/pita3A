import cv2 as cv 
import fonction as f1
import tkinter
import PIL.Image, PIL.ImageTk
import time
import numpy as np

classCascadefacial = cv.CascadeClassifier('cascade.xml')
class Video:

    def __init__(self, video_source=0):
        self.webcam = cv.VideoCapture(video_source)
        if not self.webcam.isOpened():
            raise ValueError("Unable to open video source", video_source)

        self.width = self.webcam.get(cv.CAP_PROP_FRAME_WIDTH)
        self.height = self.webcam.get(cv.CAP_PROP_FRAME_HEIGHT)
        self.x=0
    
    def get_frame(self, _haarclass ):
        if self.webcam.isOpened():
                bImgReady, imageframe = self.webcam.read() # get frame per frame from the webcam
                if bImgReady:
                    self.face = self.colordetect(imageframe,22,93,0, 45, 255, 255)
                    #self.face = self.DetectionAndMark(imageframe, _haarclass)
                    return (bImgReady, cv.cvtColor(self.face, cv.COLOR_BGR2RGB))
    
                else:
                    return (bImgReady, None)
        else:
            bImgReady   

    def __del__(self):
        if self.webcam.isOpened():
                self.webcam.release()

    def DetectionAndMark(self, _image, _classCascade):
        self.imgreturn = _image.copy()
        self.gray = cv.cvtColor(self.imgreturn, cv.COLOR_BGR2GRAY)
        

        self.reco = _classCascade.detectMultiScale(
            self.gray,
            scaleFactor=2,
            minNeighbors=5,
            minSize=(10, 10),
            flags = cv.CASCADE_SCALE_IMAGE
        )
        for (self.x, self.y, self.w, self.h) in self.reco:
            cv.rectangle(self.imgreturn, (self.x, self.y), (self.x+self.w, self.y+self.h), (0, 255, 0), 2)
            self.xcopy=self.x
            if self.x==0 :
                self.data=1
            print('%s' %self.x)
        return self.imgreturn

    def colordetect(self, _image, low1,low2,low3, high1, high2, high3):
        imageFrame =  _image.copy()
        hsvFrame = cv.cvtColor(imageFrame, cv.COLOR_BGR2HSV)
        lower = np.array([low1, low2, low3], np.uint8)
        upper = np.array([high1, high2, high3], np.uint8)
        mask = cv.inRange(hsvFrame, lower, upper)
        kernal = np.ones((5, 5), "uint8")
        mask = cv.dilate(mask, kernal)
        res = cv.bitwise_and(imageFrame, imageFrame, mask = mask)
        contours, hierarchy = cv.findContours(mask,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
        for pic, contour in enumerate(contours):
             area = cv.contourArea(contour)
             if(area > 300):
                 x, y, w, h = cv.boundingRect(contour)
                 imageFrame = cv.rectangle(imageFrame, (x, y), (x + w, y + h), (0, 0, 255), 2)
        return imageFrame  


          



class App:
    def __init__(self, window, window_title, video_source=0):
         self.window = window
         self.window.title(window_title)
         self.video_source = video_source
         self.vid = Video(self.video_source)
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
    

App(tkinter.Tk(), "Tkinter and OpenCV")







