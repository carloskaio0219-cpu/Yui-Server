from flask import Flask, jsonify

app = Flask(__name__)

@app.route("/")
def inicio():

    return jsonify({
        "status": "online",
        "nome": "Yui",
        "versao": "0.1"
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)
