from flask import Flask, request
from flask_cors import CORS

app = Flask(__name__)

CORS(app)


@app.route('/', methods=['POST'])
def result():
    print(request)  # should display 'bar'
    return 'Received !'  # response to your request.


if __name__ == "__main__":
    app.run(host='0.0.0.0')
