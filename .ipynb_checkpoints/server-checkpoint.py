from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/greet', methods=['GET'])
def greet():
    return jsonify({"message": "Merhaba Oktay!"})

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    app.run(host='0.0.0.0', port=port)
