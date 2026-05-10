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

    self.sendButton=tkinter.Button(self.frame[3],text='发送',width=10,command=self.sendMessage)
    self.sendButton.pack(expand=1,side=tkinter.BOTTOM and tkinter.RIGHT,padx=25,pady=5)

    self.closeButton=tkinter.Button(self.frame[3],text='关闭',width=10,command=self.close)
    self.closeButton.pack(expand=1,side=tkinter.RIGHT,padx=25,pady=5)
    self.frame[3].pack(expand=1,fill=tkinter.BOTH)

def receiveMessage(self):

    self.serverSocket = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
    self.serverSocket.bind((self.local,self.port))
    self.serverSocket.listen(15)
    self.buffer = 1024
    self.chatText.insert(tkinter.END,'服务器已经就绪')
    while True:
        clientSocket, clientAddress = self.serverSocket.accept()
