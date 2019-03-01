from flask import Flask, jsonify
import random

from quotes import who_quotes


app = Flask(__name__)


@app.route("/api/who/")
def serve_who_quote():
    quotes = who_quotes()
    quotes_amount = len(quotes)
    selected_quote = quotes[random.randint(0, quotes_amount - 1)]
    return jsonify(selected_quote)


if __name__ == "__main__":
    app.run(debug=True)
