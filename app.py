from flask import Flask, request, render_template
from flask_cors import CORS, cross_origin
from flask_restful import Api, Resource
from flask_jsonpify import jsonify
from Controllers.controller_employee import Employees, Employees_Name
import mimetypes

mimetypes.add_type('text/css', '.css')
mimetypes.add_type('text/javascript', '.js')
mimetypes.add_type('image/jpeg', '.jpg')
mimetypes.add_type('image/jpeg', '.jpeg')
mimetypes.add_type('image/jpeg', '.jfif')
mimetypes.add_type('image/jpeg', '.jfi')
mimetypes.add_type('image/png', '.png')
mimetypes.add_type('image/vnd.microsoft.icon', '.ico')

app = Flask(__name__,
            static_url_path='',
            static_folder='ClientApp/dist')
api = Api(app, prefix='/api')

CORS(app)

api.add_resource(Employees, '/employees')
api.add_resource(Employees_Name, '/employees/<employee_id>')
# @app.route("/")
# def hello():
#     # return render_template('index.html')
# return jsonify({'text': 'Hello World!'})


@app.route("/heartbeat")
def heartbeat():
    return jsonify({"status": "healthy"})


@app.route('/', defaults={'path': ''})
@app.route('/<path:path>')
def catch_all(path):
    return app.send_static_file("index.html")


# if
# __import__('app_ngbuild')
if __name__ == '__main__':
    app.run(port=5002)
