import socket
import threading
import time
server = 'localhost'
port = '65444'
with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as slave:
    