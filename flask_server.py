from flask import Flask

app = Flask(__name__)

@app.route("/") # decorator
def home():
    return "Hello World! I am python programmer!"

if __name__ == "__main__":
    app.run(debug=True, port=8002)