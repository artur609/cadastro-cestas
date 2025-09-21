from flask import Flask, render_template, request, redirect, url_for
import datetime

app = Flask(__name__)
cadastros = []

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        nome = request.form['nome']
        endereco = request.form['endereco']
        observacao = request.form['observacao']
        cadastro = {
            "nome": nome,
            "endereco": endereco,
            "observacao": observacao,
            "data_cadastro": datetime.datetime.now(),
            "cestas_recebidas": []
        }
        cadastros.append(cadastro)
        return redirect(url_for('lista'))
    return render_template('index.html')

@app.route('/entrega', methods=['POST'])
def entrega():
    nome = request.form['nome']
    cesta = request.form['cesta']
    for cadastro in cadastros:
        if cadastro["nome"] == nome:
            cadastro["cestas_recebidas"].append({
                "descricao": cesta,
                "data_entrega": datetime.datetime.now()
            })
            break
    return redirect(url_for('lista'))

@app.route('/lista')
def lista():
    return render_template('lista.html', cadastros=cadastros)

if __name__ == '__main__':
    app.run(debug=True)