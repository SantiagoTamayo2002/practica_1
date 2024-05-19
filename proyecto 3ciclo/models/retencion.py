from datetime import datetime
import json

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
        return round(retencion, 2)

    def generar_retencion(self, factura):
        from models.historial import Historial  
        if self.__historial_retenciones is None:
            self.__historial_retenciones = Historial()
        retencion = self.calcular_retencion(factura)
        fecha = datetime.now().strftime("%Y-%m-%d")
        identificador = self.__contador_id  # Utilizamos el contador como identificador
        self.__contador_id += 1  # Incrementamos el contador para el próximo identificador
        self.__historial_retenciones.push({"N. retenciòn": identificador,"fecha": fecha, "retencion": retencion})
        print(f"Retencion generada: {retencion}")

