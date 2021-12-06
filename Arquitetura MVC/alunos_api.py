from flask import Flask, json, request, jsonify, Blueprint

alunos_app = Blueprint('alunos_app', __name__,
                       template_folder='template')

database = {
    'ALUNO': [{"id": 1, "nome": "Andreia"},
              {"id": 2, "nome": "Arthur"},
              {"id": 3, "nome": "Pedro"}]
}

@alunos_app.route("/alunos")
def listar_alunos():
    return jsonify(database["ALUNO"])

@alunos_app.route("/alunos", methods=["POST"])
def inserir_alunos():
    novo_aluno = request.json
    database["ALUNO"].append(novo_aluno)
    return jsonify(database["ALUNO"])

@alunos_app.route("/alunos/<int:id_aluno>", methods=["DELETE"])
def excluir_aluno(id_aluno):
    for aluno in database["ALUNO"]:
        if aluno["id"] == id_aluno:
            database["ALUNO"].remove(aluno)
            return jsonify(database["ALUNO"])
    return 'Aluno não encontrado', 404

@alunos_app.route("/alunos/<int:id_aluno>", methods=["PUT"])
def atualizar_aluno(id_aluno):
    atualiza_aluno = request.get_json()
    for aluno in database["ALUNO"]:
        if aluno["id"] == id_aluno:
            database["ALUNO"].remove(aluno)
            database["ALUNO"].append(atualiza_aluno)
            return jsonify(database["ALUNO"])
    return 'Aluno não encontrado', 404

@alunos_app.route("/alunos/<int:id_aluno>", methods=["GET"])
def localizar_aluno(id_aluno):
    for aluno in database["ALUNO"]:
        if aluno["id"] == id_aluno:
            return jsonify(aluno)
    return "Aluno não encontrado", 404

@alunos_app.route("/reseta", methods=["POST"])
def resetar():
    database["ALUNO"] = []
    return jsonify(database)

@alunos_app.route("/listar_todos")
def listar_todos():
    return jsonify(database)

@alunos_app.route("/")
def start():
    return "Vamos integrar Requests e Flask"
