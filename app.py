from vidstream import *
import tkinter as tk
import socket
import threading
import requests

local_ip_addr = socket.gethostbyname(socket.gethostname())
public_ip_addr = requests.get("https://api.ipify.org").text

print(local_ip_addr)
print(public_ip_addr)