from datetime import datetime

class Retencion():
    def __init__(self):
        self.__historial_retenciones = None  
        self.__contador_id = 1
        self.__fecha = datetime.now().strftime("%Y-%m-%d")

    @property
    def _fecha(self):
        return self.__fecha

    @_fecha.setter
    def _fecha(self, value):
        self.__fecha = value


    @property
    def _contador_id(self):
        return self.__contador_id

    @_contador_id.setter
    def _contador_id(self, value):
        self.__contador_id = value


    @property
    def _historial_retenciones(self):
        return self.__historial_retenciones

    @_historial_retenciones.setter
    def _historial_retenciones(self, value):
        self.__historial_retenciones = value

    def calcular_retencion(self, factura):
        retencion = 0.0
        if factura._ructype == "educativo":
            retencion = factura._total * 0.08
        elif factura._ructype == "profesional":
            retencion = factura._total * 0.10
        else:
            print("tipo de ruc no válido")
            return None
        
        # Creamos un diccionario con las retenciones y la información de la factura
        retencion_info = {
            "retencion": round(retencion, 2),
            "factura": factura.serializer()
        }
        return retencion_info
    
    
    def to_dictionary(self):
        retencion_dict = {
            "fecha": self.__fecha,
            "contador_id": self.__contador_id,
            "historial_retenciones": self.__historial_retenciones
        }
        return retencion_dict
