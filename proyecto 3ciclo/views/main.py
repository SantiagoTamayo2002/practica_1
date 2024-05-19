import sys
sys.path.append('../')
from models.persona import Persona
from models.factura import Factura
from models.retencion import Retencion
from controls.DAO.historialDao import HistorialDao


daoHistorial = HistorialDao()
#--------------------------------------------------------------
persona_1 = Persona("Juan", "Perez", "1234567890")
persona_1.serializer()
persona_2 = Persona("Maria", "Gonzales", "0987654321")
persona_2.serializer()
#--------------------------------------------------------------
# Crear facturas
#--------------------------------------------------------------
factura_1 = Factura("1", persona_1, "profesional", 234.0)
factura_1.serializer()
factura_2 = Factura("2", persona_1, "educativo", 234.0)
factura_2.serializer()
factura_3 = Factura("3", persona_2, "profesional", 234.0)
factura_3.serializer()
#--------------------------------------------------------------
# Generar retenciones
#--------------------------------------------------------------
managerRetention = Retencion()
print("--------------------------------------------------------------")
managerRetention.generar_retencion(factura_1)
managerRetention.generar_retencion(factura_2)
managerRetention.generar_retencion(factura_3)
managerRetention._historial_retenciones.print()


