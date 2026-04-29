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

