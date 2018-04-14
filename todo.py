from flask import Flask, jsonify

app = Flask('todo')

tarefas = ['id':, '1', 'titulo':, 'descrição',
            'estado': 'false']


@app.route('/tarefas')
def listar():
    return jsonify(tarefas)