import sys
sys.path.append('../')
from datetime import datetime
from models.persona import Persona
from models.factura import Factura
from models.retencion import Retencion
import json

persona_1 = Persona("Juan", "Perez", "1234567890")
persona_1.serializer()

factura_1 = Factura("1", datetime.now(), persona_1, "profesional", 234.0)
print(factura_1.serializer())
factura_2 = Factura("2", datetime.now(), persona_1, "educativo", 234.0)
print(factura_1.serializer())
print("///////////////////////////////////////////////////////////////////")
managerRetention = Retencion()
managerRetention.calcular_retencion(factura_1)
managerRetention.generar_retencion(factura_1)
managerRetention.calcular_retencion(factura_2)
managerRetention.generar_retencion(factura_2)
print("///////////////////////////////////////////////////////////////////")

print(json.dumps(managerRetention._historial_retenciones.print, indent=4))






