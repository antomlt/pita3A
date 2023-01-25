import wx
import threading
import video

class MainFrame(wx.Frame):
    def __init__(self, parent):
        wx.Frame.__init__(self, parent)
        # Initialisation de l'interface graphique

    def UpdateIHM(self):
        # Mise à jour de l'interface graphique
        pass

class XVApp(wx.App):
    def OnInit(self):
        self.frame = MainFrame(None)
        self.frame.Show()
        self.frame.UpdateIHM()
        self.SetTopWindow(self.frame)
        
        self.camera_thread = threading.Thread(target=self.RunCamera)
        self.camera_thread.start()
        return True

    def RunCamera(self):
        my_camera = video()
        my_camera.Run()

if __name__ == '__main__':
    app = XVApp(0)
    app.MainLoop()
