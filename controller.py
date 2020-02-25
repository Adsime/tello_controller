from socket import socket
from enum import Enum

class Controller:   

    def __init__(self, socket: socket, command_address: tuple):
        self.socket = socket
        self.command_address = command_address

    def do(self, command: str):
        accept_str = "command".encode("utf-8")
        self.socket.sendto(accept_str, self.command_address)
        command = command.encode(encoding="utf-8")
        self.socket.sendto(command, self.command_address)

    def takeoff(self):
        self.do("takeoff")

    def land(self):
        self.do("land")

    def rc(self, motion):
        self.do(F"rc {motion[0]} {motion[1]} {motion[2]} {motion[3]}")

    def stream(self):
        self.do("streamon")