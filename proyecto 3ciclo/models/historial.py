from controls.TDA.stack.stack import Stack
from models.retencion import Retencion

class Historial():
    def __init__(self) -> None:
        self.__historial = Stack(20)

    def push(self, retencion: Retencion):
        self.__historial.push(retencion)

    
    def print(self):
        self.__historial.print

    def size(self):
        return self.__historial.length
    
    def serialize(self):
        return {
            "historial": self.__historial
        }
