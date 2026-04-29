import tkinter
import tkinter.font as tkFont
import socket
import threading
import time
class serverUI():

    local = '127.0.0.1'
    port = 5505
    global serverSocket
    flag = False

def __init__(self):
    self.root = tkinter.Tk()
    self.root.title('python在线聊天-服务端')
    self.frame = [tkinter.Frame(),tkinter.Frame(),tkinter.Frame(),tkinter.Frame()]
    self.chatTextScrollBar = tkinter.Scrollbar(self.frame[0])
    self.chatTextScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)
    ft=tkFont.Font(family='Fixdsys',size=11)
    self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
    self.chatText.Pack(expand=1,fill=tkinter.BOTH)
    label = tkinter.Label(self.frame[1],height=2)

