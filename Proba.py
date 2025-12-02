from flask import Flask

app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello DevOps from feature branch! 🎉"

if __name__ == "__main__":
    # 0.0.0.0: minden hálózati interfészen figyel
    # port=8080: így lesz elérhető a http://localhost:8080 címen
    app.run(host="0.0.0.0", port=8080)
