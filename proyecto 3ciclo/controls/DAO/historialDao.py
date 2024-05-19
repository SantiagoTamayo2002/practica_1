from typing import List
from models.historial import Historial  
from controls.DAO.daoAdapter import DaoAdapter

class HistorialDao:
    def __init__(self):
        self.dao_adapter = DaoAdapter(Historial)

    def guardar_retencion(self, retencion_data: dict):
        # Guardar la información de la retención en el historial
        self.dao_adapter._save(retencion_data)

    def actualizar_retencion(self, retencion_data: dict, pos: int):
        # Actualizar la información de la retención en el historial en una posición específica
        self.dao_adapter._merge(retencion_data, pos)

    def obtener_historial(self) -> List[dict]:
        # Obtener el historial completo de retenciones
        return self.dao_adapter.to_dict()

    def cargar_historial(self):
        # Cargar el historial desde el archivo JSON
        self.dao_adapter._list()

    def obtener_ultimo_id(self) -> int:
        # Obtener el último ID utilizado en el historial
        historial = self.obtener_historial()
        if historial:
            return max(item['id'] for item in historial)
        else:
            return 0

    def generar_id(self) -> int:
        # Generar un nuevo ID para una nueva retención
        return self.obtener_ultimo_id() + 1
