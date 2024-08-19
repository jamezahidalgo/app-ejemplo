from flask import Flask

app = Flask(__name__)

@app.route("/")
def inicio():
    return "Bienvenido"
    
if __name__ == '__main__':
    app.run(port=5000)
    