from PyQt5.QtCore import *
from GameClient import *
from time import *

class LoopThread(QThread, GameClient):
    # start signaling
    game_signal = pyqtSignal(str)     # create signal
    
    # construct of the class which init inherited classes
    def __init__(self):
        super(LoopThread, self).__init__()
        GameClient.__init__(self)
            
    def connect_(self, ip_address):  # Connection to server
        while True:
            while True:
                try:
                    self.connect_to_server(ip_address)
                    break
                except Exception as arr:
                    print(arr)
                    break
            break    # breaking the outer loop    
        
    # start the thread and keeps recieving messages from clients and send signals    
    def run(self):
        while True:
            msg = self.receive_message()
            if len(msg): self.game_signal.emit(str(msg))
            else: break
                
