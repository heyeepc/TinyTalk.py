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
    
