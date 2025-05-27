from flask import Flask, request, jsonify
from app import get_definition

app = Flask(__name__)

@app.route("/define", methods=["GET"])
def define():
    word = request.args.get("word")
    if not word:
        return jsonify({"error": "Kelime girilmedi."}), 400
    definitions = get_definition(word)
    return jsonify({"word": word, "definitions": definitions})

if __name__ == "__main__":
    app.run(debug=True)
