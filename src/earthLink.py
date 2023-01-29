from src import *

import socket

class EarthLink:

    _ip     : str   = '127.0.0.1'
    _port   : int   = 3333

    _deplacement: Deplacement
    _socket     : socket
    _client     : socket

    def __init__(self, deplacement:Deplacement) -> None:
        self._deplacement = deplacement

    def __enter__(self) -> 'EarthLink':
        self._socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self._socket.bind((self._ip, self._port))
        self._socket.listen()

        return self

    def __exit__(self) -> None:
        self._client.close()
        self._socket.close()

    def waitClient(self):
        self._client, adresse_client = self._socket.accept()
        print(f"connexion client : '{adresse_client}'")

    def listenInstructions(self) -> None:

        inputLink = self._client.recv(1024).decode()
        print(f"Input from Earth : {inputLink}")

        instructions    = Instructions(value=inputLink)
        message         = instructions.createCommandList(deplacement=self._deplacement)

        self._client.send(bytes(str(message), "utf-8"))