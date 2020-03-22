from flask_restful import Resource
from flask_jsonpify import jsonify


class Employees(Resource):
    def get(self):
        return {'employees': [{'id': 1, 'name': 'Balram'}, {'id': 2, 'name': 'Tom'}]}


class Employees_Name(Resource):
    def get(self, employee_id):
        print('Employee id:' + employee_id)
        result = {'data': {'id': 1, 'name': 'Balram'}}
        return jsonify(result)
