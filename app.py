from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def login():
    return "SIGEM-DPS iniciado com sucesso!"

if __name__ == "__main__":
    app.run(debug=True)
