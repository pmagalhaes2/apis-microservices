from flask import Flask

app = Flask(__name__)

@app.route("/<float(signed=True):a>/divide/<float(signed=True):b>")
@app.route("/<float(signed=True):a>/divide/<int(signed=True):b>")
@app.route("/<int(signed=True):a>/divide/<int(signed=True):b>")
@app.route("/<int(signed=True):a>/divide/<float(signed=True):b>")

def dividir(a, b):
    if b == 0: return "Não é possível realizar divisão por zero!", 422
    return str(a/b)


@app.route("/<float(signed=True):a>/soma/<float(signed=True):b>")
@app.route("/<float(signed=True):a>/soma/<int(signed=True):b>")
@app.route("/<int(signed=True):a>/soma/<int(signed=True):b>")
@app.route("/<int(signed=True):a>/soma/<float(signed=True):b>")

def somar(a, b):
    return str(a + b)


if __name__ == "__main__":
    app.run(host="localhost", port=5000, debug=True)

