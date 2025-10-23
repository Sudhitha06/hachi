import socket
import random
import time

s = socket.socket()
s.bind(("localhost", 8038))
s.listen(5)
c, adr = s.accept()
print("From address", str(adr), "connection has established")

n = int(input("Enter number of frames: "))
N = int(input("Enter window size: "))

seq = 1
frame = 1

# Send first N frames
for i in range(N):
    print('Frames sent ->', frame)
    c.send(str(frame).encode())
    frame += 1
    time.sleep(2)

timer = 5

while frame <= n:
    t = random.randint(1, 7)
    msg = c.recv(2).decode()
    msg = int(msg)
    print("Frame", msg)

    if timer > t:
        print("Acknowledgement received")
        print('Frames sent ->', frame)
        c.send(str(frame).encode())
        seq += 1
        frame += 1
        time.sleep(2)
    else:
        print("Acknowledgement not received")
        print('Frames sent ->', msg)
        c.send(str(msg).encode())
        time.sleep(2)

import socket
import time

s = socket.socket()
s.connect(("localhost", 8038))

while True:
    msg = s.recv(2).decode()
    print("Received -->", int(msg))
    s.send(str(msg).encode())
    time.sleep(1)


