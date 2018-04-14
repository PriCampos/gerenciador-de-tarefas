from flask import Flask, jsonify

app = Flask('todo')

tarefas = {'id': 1, 'titulo': 'descricao',
            'estado': 'false'}


@app.route('/tarefas')
def listar():
    return jsonify(tarefas)