from flask import Flask, jsonify, make_response, redirect
app = Flask(__name__)

@app.route("/exemplo5")
def exemplo_5():
    x = jsonify(["abacaxi", "uva", "morango"])
    r = make_response(x)
    r.headers["X-tipo-dado"] = "frutas"
    r.status_code = 275
    return r

@app.route("/exemplo6")
def exemplo_6():
    # Se o code for omitido, o 302 seria utilizado por padrão
    return redirect("/exemplo5", code = 305)

if __name__ == "__main__":
    app.run(host = "localhost", port = 5002)
