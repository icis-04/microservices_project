from ipaddress import ip_address
from flask import Flask, jsonify, render_template
import socket

app = Flask(__name__)

# function that gets hostname and ip
def getDetails():
    orchestration = "Kubernetes"

    return orchestration


@app.route("/")
def hello_world():
    return "<p>Hello, World!</p>"


@app.route("/health")
def diabetes():
    return jsonify(status="UP")


@app.route("/obj")
def objective():
    cncf = getDetails()
    return render_template("index.html", cncf=cncf)


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=True)
