import tkinter as tk
from tkinter import scrolledtext, messagebox
import socket
import threading
import time


class ModernServer:
    def __init__(self):
        self.root = tk.Tk()
        self.root.title("Python 现代聊天服务端 2.0")
        self.root.geometry("500x600")
        self.root.configure(bg="#f0f2f5")  # 浅灰色背景，更有现代感

        # 网络参数
        self.host = '127.0.0.1'
        self.port = 5505
        self.conn = None  # 保存客户端连接

        self.setup_ui()

    def setup_ui(self):
        """构建界面布局"""
        # 1. 顶部标题
        tk.Label(self.root, text="聊天服务器 - 已就绪", font=("微软雅黑", 12, "bold"),
                 bg="#3b5998", fg="white", pady=10).pack(fill=tk.X)

        # 2. 聊天记录区 (使用 ScrolledText 自动集成滚动条)
        self.display_area = scrolledtext.ScrolledText(self.root, font=("微软雅黑", 10), state='disabled')
        self.display_area.pack(padx=10, pady=10, fill=tk.BOTH, expand=True)
        # 给文本框上色
        self.display_area.tag_config("server", foreground="#007bff")  # 蓝色代表服务器
        self.display_area.tag_config("client", foreground="#28a745")  # 绿色代表客户端
        self.display_area.tag_config("system", foreground="#6c757d", font=("微软雅黑", 9, "italic"))

        # 3. 输入区
        input_frame = tk.Frame(self.root, bg="#f0f2f5")
        input_frame.pack(fill=tk.X, padx=10, pady=(0, 10))

        self.input_box = tk.Text(input_frame, height=4, font=("微软雅黑", 10), bd=1, relief="flat")
        self.input_box.pack(side=tk.LEFT, fill=tk.X, expand=True, padx=(0, 10))

        # 绑定回车键发送
        self.input_box.bind("<Return>", lambda e: self.send_message())

        # 4. 按钮区
        btn_frame = tk.Frame(input_frame, bg="#f0f2f5")
        btn_frame.pack(side=tk.RIGHT)

        tk.Button(btn_frame, text="发送 (Enter)", command=self.send_message,
                  bg="#28a745", fg="white", relief="flat", width=10, pady=5).pack(side=tk.TOP)
        tk.Button(btn_frame, text="关闭服务", command=self.root.quit,
                  bg="#dc3545", fg="white", relief="flat", width=10, pady=5).pack(side=tk.BOTTOM, pady=(5, 0))

    def log(self, sender, message, tag="system"):
        """向界面插入消息的统一函数"""
        self.display_area.configure(state='normal')  # 解锁编辑
        curr_time = time.strftime('%H:%M:%S')
        if sender:
            self.display_area.insert(tk.END, f"[{curr_time}] {sender}:\n", tag)
            self.display_area.insert(tk.END, f"{message}\n\n")
        else:
            self.display_area.insert(tk.END, f"系统: {message}\n", tag)

        self.display_area.configure(state='disabled')  # 重新锁定
        self.display_area.see(tk.END)  # 自动滚动到底部

    def start_network(self):
        """启动网络监听线程"""
        thread = threading.Thread(target=self.receive_loop, daemon=True)
        thread.start()

    def receive_loop(self):
        server_sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        # 允许端口即时复用，防止重启程序时显示“端口被占用”
        server_sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server_sock.bind((self.host, self.port))
        server_sock.listen(1)

        self.log(None, "等待客户端连接...")

        while True:
            try:
                self.conn, addr = server_sock.accept()
                self.log(None, f"来自 {addr} 的连接已建立")

                while True:
                    data = self.conn.recv(1024).decode('utf-8')
                    if not data: break
                    self.log("客户端", data, "client")
            except Exception as e:
                self.log(None, f"连接异常断开: {e}")
                break

    def send_message(self):
        if not self.conn:
            messagebox.showwarning("警告", "当前没有客户端连接！")
            return

        msg = self.input_box.get("1.0", tk.END).strip()
        if msg:
            try:
                self.conn.send(msg.encode('utf-8'))
                self.log("服务器(我)", msg, "server")
                self.input_box.delete("1.0", tk.END)
            except:
                self.log(None, "消息发送失败，连接可能已关闭")
        return "break"  # 防止 Text 组件在回车后换行


if __name__ == "__main__":
    app = ModernServer()
    app.start_network()  # 启动后台监听
    app.root.mainloop()  # 进入主循环