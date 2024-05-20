import sys
sys.path.append('../')
from flask import Blueprint, jsonify, make_response, request
from views.main import ret_1, ret_2, ret_3
from controls.historialControl import Historial
from models.factura import Factura
api = Blueprint('api', __name__)




@api.route('/')
def home():
    return make_response(
    jsonify({"msg":"OK", "code": 200}),
    200
    )


@api.route('/api/retenciones')
def lista_retenciones():
    retenciones_list = Historial()
    retenciones_list.push(ret_1)
    retenciones_list.push(ret_2)
    retenciones_list.push(ret_3)
    return make_response(
    jsonify({"msg":"OK", "code": 200, "data": retenciones_list.save_to_json("historial.json")}),
    200
    )

@api.route('/api/guardarFactura', methods=['POST'])
def guardar_factura():
    data = request.get_json()
    factura = Factura()
    factura.deserializer(data)
    return make_response(
    jsonify({"msg":"OK", "code": 200, "data": factura.serializer()}),
    200
    )
