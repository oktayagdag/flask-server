from flask import Flask, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return "Server ayakta! 🚀"

@app.route('/greet')
def greet():
    return jsonify({"message": "Merhaba Oktay!"})

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)