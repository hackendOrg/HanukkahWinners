from flask import Flask, request
from flask_cors import CORS

from score_board import ScoreBoard

app = Flask(__name__)

CORS(app)

score_board = ScoreBoard()


@app.route('/', methods=['POST'])
def result():
    score_board.add(request.form['name'], request.form['score'])
    return 'Received !'  # response to your request.


if __name__ == "__main__":
    app.run(host='0.0.0.0')
