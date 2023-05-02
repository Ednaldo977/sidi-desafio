
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
   
conn = psycopg2.connect(
    host="localhost",
    database="Vagas",
    user="postgres",
    password="post23"
)


cursor = conn.cursor()

@app.route('/resposta_eliminatoria', methods=['POST'])
def resposta_eliminatoria():
    # Obtém os dados enviados no corpo da requisição
    data = request.get_json()

    # Obtém os valores das chaves do dicionário 'data' (nome, email e formacao)
    experiencia = data.get('Você tem experiência na área desejada')
    conhecimento_ingles = data.get('Você tem conhecimento do idioma inglês intermediário / avançado?')
    conhecimento_python = data.get('Você tem conhecimento em python?')

    # Insere os dados recebidos na tabela job_application
    cursor.execute('''
        INSERT INTO resposta_eliminatoria (
            experiencia,
            conhecimento_ingles,
            conhecimento_python
        ) VALUES (
            %s, %s, %s
        )
    ''', (
        experiencia,
        conhecimento_ingles,
        conhecimento_python
    ))

    conn.commit()  # Salva as alterações no banco de dados

    return jsonify({'status': 'ok'})
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++

conn = psycopg2.connect(
    host="localhost",
    database="Vagas",
    user="postgres",
    password="post23"
)

cursor = conn.cursor()

@app.route('/resposta_obrigatoria', methods=['POST'])
def resposta_obrigatoria():
    # Obtém os dados enviados no corpo da requisição
    data = request.get_json()

    # Obtém os valores das chaves do dicionário 'data' (nome, email e formacao)
    nome = data.get('Qual seu nome?')
    email = data.get('Qual seu email?')
    formacao = data.get('Qual sua formação?')

    # Insere os dados recebidos na tabela job_application
    cursor.execute('''
        INSERT INTO resposta_obrigatoria (
            nome,
            email,
            formacao
        ) VALUES (
            %s, %s, %s
        )
    ''', (
        nome,
        email,
        formacao
    ))

    conn.commit()  # Salva as alterações no banco de dados

    return jsonify({'status': 'ok'})

    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    # +++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++
    
if __name__ == '__main__':
    app.run(debug=True)
