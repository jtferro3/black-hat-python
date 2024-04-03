#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Nov 02 16:03:00 2022

@author: jtferro3
"""

import socket
target_host = "localhost"
target_port = 9998

# create a socket object
client = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
  
# send some data
client.sendto(b"AAABBBCCC",(target_host,target_port))

# receive some data
data, addr = client.recvfrom(4096)
print(data.decode())
client.close()