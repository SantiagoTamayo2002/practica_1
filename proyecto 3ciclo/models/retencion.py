from datetime import datetime
from models.factura import Factura
from controls.TDA.stack.stack import Stack


class Retencion:
    def __init__(self):
        self.__historial_retenciones = Stack(10)

    @property
    def _historial_retenciones(self):
        return self.__historial_retenciones

    @_historial_retenciones.setter
    def _historial_retenciones(self, value):
        self.__historial_retenciones = value


    def calcular_retencion(self, factura: Factura) -> float:
        retencion = 0.0
        if factura._ructype == "educativo":
            retencion = factura._total * 0.08
        elif factura._ructype == "profesional":
            retencion = factura._total * 0.10
        return round(retencion, 2)

    def generar_retencion(self, factura: Factura):
        retencion = self.calcular_retencion(factura)
        fecha = datetime.now().strftime("%Y-%m-%d")
        self.__historial_retenciones.push({"fecha": fecha, "retencion": retencion})
        print(f"Retencion generada: {retencion}")


    
