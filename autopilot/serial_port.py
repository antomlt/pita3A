import serial

class PortSerie:
    def __init__(self, i_NomPort = None):
        if i_NomPort:
            self.open(i_NomPort)

    def open(self, i_NomPort):
        self.handleSerial = serial.Serial(i_NomPort, baudrate=9600, bytesize=8, parity='E', stopbits=1)

    def close(self):
        self.handleSerial.close()

    def send(self, i_Chaine):
        print("Chaine à envoyer: ", i_Chaine)
        nBytesWritten = self.handleSerial.write(i_Chaine.encode())
        print("Nombre de bytes envoyés: ", nBytesWritten)

    def receive(self, o_chaine):
        nBytesRead = self.handleSerial.read(199)
        if nBytesRead:
            o_chaine = nBytesRead.decode()
            return 0
        else:
            return -1
