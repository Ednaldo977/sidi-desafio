
from flask import Flask, jsonify, request
import psycopg2

app = Flask(__name__)
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
# +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
@app.route('/id/<int:id>', methods=['GET'])
def get_id(id):
    conn = psycopg2.connect(
        host="localhost",
        database="Vagas",
        user="postgres",
        password="post23",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM vagas WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return jsonify({'status': 'Ok'})
    else:
        return jsonify({'status': 'Vaga não encontrada'})
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@app.route('/perguntas_eliminatorias/<int:id>', methods=['GET'])
def get_perguntas_eliminatorias(id):
    conn = psycopg2.connect(
        host="localhost",
        database="Vagas",
        user="postgres",
        password="post23",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM perguntas_eliminatorias WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return jsonify({'status': 'Ok', 'pergunta': row})
    else:
        return jsonify({'status': 'Pergunta não encontrada'})


    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

@app.route('/perguntas_obrigatorias/<int:id>', methods=['GET'])
def get_perguntas_obrigatorias(id):
    conn = psycopg2.connect(
        host="localhost",
        database="Vagas",
        user="postgres",
        password="post23",
        port="5432"
    )
    cur = conn.cursor()
    cur.execute("SELECT * FROM perguntas_obrigatorias WHERE id = %s", (id,))
    row = cur.fetchone()
    cur.close()
    conn.close()
    if row:
        return jsonify({'status': 'Ok', 'pergunta': row})
    else:
        return jsonify({'status': 'Pergunta não encontrada'})
    
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++



    
if __name__ == '__main__':
    app.run(debug=True)
