# API Flask de apoio para testar o site da livraria.
# Instalar: pip install flask flask-cors
# Rodar:    python app.py   (abre em http://localhost:5000)
import sqlite3
from flask import Flask, jsonify, request
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # libera o front-end (outra origem) a chamar a API

DB = 'livraria.db'

def conectar():
    con = sqlite3.connect(DB)
    con.row_factory = sqlite3.Row
    return con

def criar_tabela():
    with conectar() as con:
        con.execute('''CREATE TABLE IF NOT EXISTS livros (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            titulo TEXT NOT NULL, autor TEXT NOT NULL,
            genero TEXT NOT NULL, preco REAL NOT NULL)''')

@app.get('/livros')
def listar():
    with conectar() as con:
        linhas = con.execute('SELECT * FROM livros ORDER BY id DESC').fetchall()
    return jsonify([dict(l) for l in linhas])

@app.post('/livros')
def cadastrar():
    dados = request.get_json(silent=True) or {}
    campos = ['titulo', 'autor', 'genero', 'preco']
    if not all(dados.get(c) not in (None, '') for c in campos):
        return jsonify({'erro': 'Preencha título, autor, gênero e preço.'}), 400
    try:
        preco = float(dados['preco'])
    except (TypeError, ValueError):
        return jsonify({'erro': 'Preço inválido.'}), 400
    with conectar() as con:
        cur = con.execute('INSERT INTO livros (titulo, autor, genero, preco) VALUES (?,?,?,?)',
                          (dados['titulo'], dados['autor'], dados['genero'], preco))
    return jsonify({'id': cur.lastrowid, 'mensagem': 'Livro cadastrado'}), 201

if __name__ == '__main__':
    criar_tabela()
    app.run(debug=True)
