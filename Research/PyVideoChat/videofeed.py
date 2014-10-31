import cv2
from cv2.cv import *
import Image

class VideoFeed:

    def __init__(self,mode=1,name="w1",capture=1):
        print name
        if mode == 1:
            cv2.startWindowThread()
            cv2.namedWindow(name,CV_WINDOW_AUTOSIZE)
        self.camera_index = 0
        self.name = name
        if capture == 1:
            self.capture = cv2.VideoCapture(self.camera_index)

    def get_frame(self):
        self.frame = cv.QueryFrame(self.capture)
        self.c = cv.WaitKey(1)
        if(self.c=="n"): #in "n" key is pressed while the popup window is in focus
            self.camera_index += 1 #try the next camera index
            self.capture = cv.CaptureFromCAM(camera_index)
            if not self.capture: #if the next camera index didn't work, reset to 0.
                self.camera_index = 0
                self.capture = cv.CaptureFromCAM(camera_index)
        jpegImg= Image.fromstring("RGB",cv.GetSize(self.frame),self.frame.tostring())
        retStr=jpegImg.tostring("jpeg","RGB")
        print "Compressed Size = ",len(retStr)
        return retStr


    def set_frame(self,frame):
        #This function sets the picture to a desired frame size
        #self  - object of this class
        #frame - captured frame
        jpegPIL = Image.fromstring("RGB",(640,480),frame,"jpeg","RGB","raw")
        cv_im = cv.CreateImage((640,480),cv.IPL_DEPTH_8U,3)
        cv.SetData(cv_im,jpegPIL.tostring())
        cv.ShowImage(self.name,cv_im)
        
if __name__ == "__main__":
    vf = VideoFeed(1,"test",1) #initial mode,window name,capture
    while 1: #an infinite loop
        m = vf.getFrame() #Getting new frames incrementally
        vf.set_frame(m)   #putting the modified image frame into viewport
        
