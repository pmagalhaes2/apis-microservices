from flask import Flask, render_template
app = Flask(__name__)

@app.route("/")
@app.route("/bom-dia")
def bom_dia():
    return render_template("index.html", mensagem = "Bom dia!")

@app.route("/boa-tarde")
def boa_tarde():
    return render_template("index.html", mensagem = "Boa tarde!")

@app.route("/boa-noite")
def boa_noite():
    return render_template("index.html", mensagem = "Boa noite!")


if __name__ == "__main__":
    app.run(host="localhost", port=5002, debug=True)
