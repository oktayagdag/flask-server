from flask import Flask, jsonify, request

app = Flask(__name__)

@app.route('/')
def home():
    return "Server ayakta! 🚀"

@app.route('/greet')
def greet():
    return jsonify({"message": "Merhaba Oktay!"})

@app.route('/multiply', methods=['POST'])
def multiply():
    data = request.get_json()
    number1 = data.get('number1')
    number2 = data.get('number2')

    if number1 is None or number2 is None:
        return jsonify({"error": "Eksik veri gönderildi."}), 400

    try:
        result = float(number1) * float(number2)
        return jsonify({"result": result})
    except ValueError:
        return jsonify({"error": "Sayısal veri bekleniyordu."}), 400

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=10000)