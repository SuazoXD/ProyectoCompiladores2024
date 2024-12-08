from flask import Flask, render_template, request
from parser import analizar

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    resultado = None
    if request.method == "POST":
        codigo = request.form["code"]
        resultado = analizar(codigo)
    
    # Si resultado existe, retornamos detalles para el HTML
    if resultado:
        return render_template("index.html", 
                               result={
                                   'lexical': resultado['lexical'],
                                   'syntax': resultado['syntax'],
                                   'operation': resultado['operation']
                               })
    return render_template("index.html", result=None)

if __name__ == "__main__":
    app.run(debug=True)
