import serial

class Radio:
    def __init__(self):
        self.Load()
        self.Open(self.m_NomPort)
        self.Reset()

    def __del__(self):
        self.m_Port.close()
        self.Save()

    def SetDefault(self):
        self.m_Mode = "NORM"
        self.m_NomPort = "COM1"
        self.m_TrimA = 0
        self.m_TrimE = 0
        self.m_TrimR = 0
        self.m_TrimT = 0

    def Load(self):
        try:
            with open("Radio.cfg", "r") as file:
                data = file.readline()
                data = data.strip().split(",")
                self.m_NomPort = data[0].replace('"','')
                self.m_Mode = data[1]
                self.m_TrimA = int(data[2])
                self.m_TrimE = int(data[3])
                self.m_TrimR = int(data[4])
                self.m_TrimT = int(data[5])
        except:
            self.SetDefault()

    def Save(self):
        try:
            with open("Radio.cfg", "w") as file:
                file.write('"{}",{},{},{},{},{}\n'.format(self.m_NomPort, self.m_Mode, self.m_TrimA, self.m_TrimE, self.m_TrimR, self.m_TrimT))
        except:
            pass

    def Open(self, i_PortName):
        self.m_Port = serial.Serial(i_PortName, baudrate=9600)
        self.m_NomPort = i_PortName

    def Close(self):
        self.m_Port.close()

    def GetNomPort(self):
        return self.m_NomPort

    def EnvoieCmd(self, cmd, value):
        print("Envoi du niveau {} avec la comande {}".format(value, cmd))
        self.m_Port.write(bytes([cmd, value]))

    def Reset(self):
        self.SetLevelT(0)
        self.ReCenter()

    def ReCenter(self):
        self.SetLevelA(50)
        self.SetLevelE(50)
        self.SetLevelR(50)

    def SetMode(self, i_Mode):
        self.m_Mode = i_Mode

    def GetMode(self):
        ...
    # The other functions such as : 
    # SetLevelA, SetLevelE, SetLevelR, SetLevelT, 
    # GetLevelA, GetLevelE, GetLevelR, GetLevelT, 
    # SetTrimA, SetTrimE, SetTrimR, SetTrimT, 
    # GetTrimA, GetTrimE, GetTrimR, GetTrimT 
    # are similar to C++ version, they can be implemented by using the same logic and using pyserial
