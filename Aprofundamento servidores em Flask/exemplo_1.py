from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/bom-dia")

def bom_dia():
    return jsonify("Bom dia")

@app.route("/uma-lista")

def uma_lista():
    return jsonify([1, 2, 3, 4, 5])

if __name__ == "__main__":
    app.run()

