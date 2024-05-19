from datetime import datetime
from models.persona import Persona

class Factura():
    def __init__(self, id: str, cliente: Persona, rucType: str, total: float):
        self.__id = id
        self.__cliente = cliente
        self.__ructype = rucType
        self.__total = total


#                               GETTERS Y SETTERS
#///////////////////////////////////////////////////////////////////////
    @property
    def _id(self):
        return self.__id

    @_id.setter
    def _id(self, value):
        self.__id = value

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value

    @property
    def _cliente(self):
        return self.__cliente

    @_cliente.setter
    def _cliente(self, value):
        self.__cliente = value

    @property
    def _ructype(self):
        return self.__ructype

    @_ructype.setter
    def _ructype(self, value):
        self.__ructype = value

    @property
    def _total(self):
        return self.__total

    @_total.setter
    def _total(self, value):
        self.__total = value

#///////////////////////////////////////////////////////////////////////

    def serializer(self):
        return{
            "id": self.__id,
            "cliente": self.__cliente.serializer(),
            "rucType": self.__ructype,
            "total": self.__total,
        }
    
    def deserializer(self, data: dict):
        self.__id = data["id"]
        self.__cliente = Persona.serializer(data["cliente"])
        self.__ructype = data["rucType"]
        self.__total = data["total"]

    #funcion para generar id de factura desde cero incrementados en 1
    def generar_id(self):
        self.__id = str(int(self.__id) + 1)
        return self.__id