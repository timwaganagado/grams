import socket
from _thread import *
import sys

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

server = '192.168.1.14'
port = 5555

server_ip = socket.gethostbyname(server)

try:
    s.bind((server, port))

except socket.error as e:
    print(str(e))

s.listen(2)
print("Waiting for a connection")

currentId = 0
pos = ['0:[ai,50,50]', "1:[ai,100,100]","2:[ai,150,150]","3:[ai,200,200]"]
def threaded_client(conn):
    global currentId, pos
    conn.send(str.encode(str(currentId)))
    currentId += 1
    reply = ''
    while True:
        try:
            data = conn.recv(2048)
            reply = data.decode('utf-8')
            if not data:
                conn.send(str.encode("Goodbye"))
                break
            else:
                arr = reply.split(":")
                print(arr)
                id = int(arr[0])
                pos[id] = reply



            conn.sendall(str.encode(str(pos)))
        except:
            break
    print(currentId)
    currentId -= 1
    print("Connection Closed")
    conn.close()

while True:
    conn, addr = s.accept()
    print("Connected to: ", addr)

    start_new_thread(threaded_client, (conn,))