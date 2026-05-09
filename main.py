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
    label.pack(fill=tkinter.BOTH)
    self.frame[1].pack(expand=1,fill=tkinter.BOTH)

    self.inputTexScrollBar = tkinter.Scrollbar(self.frame[2])
    self.inputTexScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    ft=tkFont.Font(family='Fixdsys',size=11)
    self.inputTex = tkinter.Text(self.frame[2],width=70,height=8,font=ft)
    self.inputTex['yscrollcommand'] = self.inputTexScrollBar.set
    self.inputTex.Pack(expand=1,fill=tkinter.BOTH)
    self.inputTexScrollBar['command'] = self.inputTex.yview()
    self.frame[2].pack(expand=1,fill=tkinter.BOTH)

    self.inputTexScrollBar=tkinter.Scrollbar(self.frame[2])
    self.inputTexScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

    ft=tkFont.Font(family='Fixdsys',size=11)
    self.inputTex= tkinter.Text(self.frame[2],width=70,height=8,font=ft)
    self.inputTex['yscrollcommand'] = self.inputTexScrollBar.set
    self.inputTex.Pack(expand=1,fill=tkinter.BOTH)
    self.inputTexScrollBar['command'] = self.inputTexScrollBar.yview()
    self.frame[2].pack(expand=1,fill=tkinter.BOTH)
    

