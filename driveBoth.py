from sender import transmit_message
from receiver import listenForData
from convertUtility import bytesToMessage, messageToBytes
import threading

def listen():
    listenForData(1)

def broadcast():
    while True:
        message = input("What message would like to send?")
        transmit_message(messageToBytes(message))

t1 = threading.Thread(target=listen, args=())
t2 = threading.Thread(target=broadcast, args=())

t1.start()

t2.start()

