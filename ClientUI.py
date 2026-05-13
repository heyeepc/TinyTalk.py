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
    
