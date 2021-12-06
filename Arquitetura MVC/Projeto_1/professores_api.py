from flask import Flask, json, request, jsonify, Blueprint

professores_app = Blueprint('professores_app', __name__,
                       template_folder='template')

database = {
    'PROFESSOR': [{"id": 1, "nome": "Professor1"},
                  {"id": 2, "nome": "Professor2"},
                  {"id": 3, "nome": "Professor3"}]
}

@professores_app.route("/reseta", methods=["POST"])
def resetar():
    database["PROFESSOR"] = []
    return jsonify(database)
            
@professores_app.route("/professores")
def listar_professores():
    return jsonify(database["PROFESSOR"])

@professores_app.route("/listar_todos")
def listar_todos():
    return jsonify(database)

@professores_app.route("/")
def start():
    return "Vamos integrar Requests e Flask"


