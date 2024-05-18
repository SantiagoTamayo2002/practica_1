
class Persona():
    def __init__(self, name: str, lastName: str, identification: str):
        self.__nombre = name
        self.__apellido = lastName
        self.__identificacion = identification


#                               GETTERS Y SETTERS    
#///////////////////////////////////////////////////////////////////////
    @property
    def _nombre(self):
        return self.__nombre

    @_nombre.setter
    def _nombre(self, value):
        self.__nombre = value

    @property
    def _apellido(self):
        return self.__apellido

    @_apellido.setter
    def _apellido(self, value):
        self.__apellido = value

    @property
    def _identificacion(self):
        return self.__identificacion

    @_identificacion.setter
    def _identificacion(self, value):
        self.__identificacion = value
   
#///////////////////////////////////////////////////////////////////////

    def serializer(self):
        return{
            "nombre": self.__nombre,
            "apellido": self.__apellido,
            "identificacion": self.__identificacion
        }


    
