import tkinter
import tkinter.font as tkFont
import socket
import threading
import time

class ClientUI():
    local = '172.0.0.1'
    port = 5505
    global clientSock;
    flag = False

def __init__(self):
    self.root = tkinter.Tk()
    self.root.title("python在线聊天-客户端")

    self.frame = [tkinter.Frame(),tkinter.Frame(),tkinter.Frame(),tkinter.Frame()]
    self.chatTextscrollbar = tkinter.Scrollbar(self.frame[0])
    self.chatTextscrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

    ft = tkinter.font(family='fixdsys',size = 11)
    self.chatText=tkinter.Listbox(self.frame[0],width=70,height=18,font=ft)
    self.chatText['yscrollcommand'] = self.chatTextscrollbar.set
    self.chatText.pack(expand=1,fill=tkinter.BOTH)
    self.chatTextscrollbar['command'] = self.chatText.yview()
    self.frame[1].pack(expand=1,fill=tkinter.BOTH)\

    self.inputTextScrollbar = tkinter.Scrollbar(self.frame[2])
    self.inputTextScrollbar.pack(side=tkinter.RIGHT,fill=tkinter.Y)

    ft = tkinter.font(family='fixdsys',size = 11)
    self.inputText = tkinter.Entry(self.frame[2],width=70 ,height=8,font=ft)
    self.inputText['yscrollcommand'] = self.inputTextScrollbar.set
    self.inputText.pack(expand=1,fill=tkinter.BOTH)
    self.inputTextScrollbar['command'] = self.inputText.yview()
    self.frame[2].pack(expand=1,fill=tkinter.BOTH)

    
