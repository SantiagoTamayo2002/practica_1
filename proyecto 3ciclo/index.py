from app import create_app
from flask import jsonify, make_response
from flask import request

app = create_app()

@app.after_request
def after_request(response):  # Add a function declaration after the decorator
    origin = request.headers.get('Origin')
    if request.method == 'OPTIONS':
        response = make_response()
        response.headers.add('Access-Control-Allow-Credentials', 'true')
        response.headers.add('Access-Control-Allow-Headers', 'Content-Type')
        response.headers.add('Access-Control-Allow-Headers', 'x-csrf-token')
        response.headers.add('Access-Control-Allow-Methods',
                             'GET, POST, OPTIONS, PUT, PATCH, DELETE')
    if origin:
        response.headers.add('Access-Control-Allow-Origin', origin)
    else:
        response.headers.add('Access-Control-Allow-Credentials', 'true')
    return response  # Add a return statement for the function
if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0")