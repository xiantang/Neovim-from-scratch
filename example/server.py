from flask import Flask

app = Flask(__name__)


@app.route("/")
def hello_world():
    a = 1
    b = 2
    c = a + b
    return "<p>Hello, World" + str(c) + "!</p>"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=8080)
