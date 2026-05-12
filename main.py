import sys
import tkinter
import tkinter.font as tkFont
import socket
import threading
import time


class serverUI():
    def __init__(self):
        self.local = '127.0.0.1'
        self.port = 5505
        self.flag = False

        self.root = tkinter.Tk()
        self.root.title('python在线聊天-服务端')

        # 布局框架
        self.frame = [tkinter.Frame() for _ in range(4)]

        # 1. 聊天显示区域
        self.chatTextScrollBar = tkinter.Scrollbar(self.frame[0])
        self.chatTextScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        ft = tkFont.Font(family='Fixdsys', size=11)
        self.chatText = tkinter.Text(self.frame[0], width=70, height=18, font=ft)  # 补上了创建语句
        self.chatText['yscrollcommand'] = self.chatTextScrollBar.set
        self.chatText.pack(expand=1, fill=tkinter.BOTH)  # Pack 改为 pack
        self.chatTextScrollBar['command'] = self.chatText.yview
        self.frame[0].pack(expand=1, fill=tkinter.BOTH)

        # 2. 中间标签
        label = tkinter.Label(self.frame[1], text="输入区", height=2)
        label.pack(fill=tkinter.BOTH)
        self.frame[1].pack(expand=1, fill=tkinter.BOTH)

        # 3. 输入区域
        self.inputTexScrollBar = tkinter.Scrollbar(self.frame[2])
        self.inputTexScrollBar.pack(side=tkinter.RIGHT, fill=tkinter.Y)

        self.inputTex = tkinter.Text(self.frame[2], width=70, height=8, font=ft)
        self.inputTex['yscrollcommand'] = self.inputTexScrollBar.set
        self.inputTex.pack(expand=1, fill=tkinter.BOTH)
        self.inputTexScrollBar['command'] = self.inputTex.yview
        self.frame[2].pack(expand=1, fill=tkinter.BOTH)

        # 4. 按钮区域
        self.sendButton = tkinter.Button(self.frame[3], text='发送', width=10, command=self.sendMessage)
        self.sendButton.pack(side=tkinter.RIGHT, padx=25, pady=5)

        self.closeButton = tkinter.Button(self.frame[3], text='关闭', width=10, command=self.close)
        self.closeButton.pack(side=tkinter.RIGHT, padx=25, pady=5)
        self.frame[3].pack(expand=1, fill=tkinter.BOTH)

    def receiveMessage(self):
        self.serverSocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.serverSocket.bind((self.local, self.port))
        self.serverSocket.listen(15)
        self.buffer = 1024
        self.chatText.insert(tkinter.END, '服务器已经就绪...\n')

        while True:
            self.connection, self.address = self.serverSocket.accept()
            self.flag = True
            while True:
                try:
                    clientMsg = self.connection.recv(self.buffer).decode('utf-8')
                    if not clientMsg:
                        break

                    if clientMsg == 'y':
                        self.chatText.insert(tkinter.END, '系统：客户端请求连接成功\n')
                        self.connection.send(b'y')
                    else:
                        theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
                        self.chatText.insert(tkinter.END, f'客户端 {theTime} 说：\n{clientMsg}\n')
                except:
                    break

    def sendMessage(self):
        # 应该从 inputTex 获取待发送的消息
        message = self.inputTex.get('1.0', tkinter.END).strip()
        if not message:
            return

        theTime = time.strftime('%Y-%m-%d %H:%M:%S', time.localtime())
        self.chatText.insert(tkinter.END, f'服务器 {theTime} 说：\n{message}\n')

        if self.flag:
            self.connection.send(message.encode('utf-8'))
            self.inputTex.delete('1.0', tkinter.END)  # 发送后清空输入框
        else:
            self.chatText.insert(tkinter.END, '错误：未建立连接，发送失败\n')

    def close(self):
        self.root.destroy()
        sys.exit()

    def startNewThread(self):
        thread = threading.Thread(target=self.receiveMessage)
        thread.daemon = True  # 设置守护线程
        thread.start()


def main():
    server = serverUI()
    server.startNewThread()
    server.root.mainloop()


if __name__ == '__main__':
    main()