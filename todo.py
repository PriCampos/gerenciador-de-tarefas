from flask import Flask, jsonify

app = Flask('todo')

tarefas = []


@app.route('/tarefas')
def listar():
    return jsonify(tarefas)