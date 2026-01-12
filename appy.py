from flask import Flask, request, jsonify
import pandas as pd
import math
app = Flask(__name__)
@app.route("/", methods=["GET"])
def home():
    return """
    <h2>Debiut – kierowcy</h2>
    <form action="/upload" method="post" enctype="multipart/form-data">
        <input type="file" name="file" required>
        <button type="submit">Wyznacz trasy</button>
    </form>
    """
@app.route("/upload", methods=["POST"])
def upload():
    file = request.files["file"]
    df = pd.read_excel(file)
    addresses = df["address"].tolist()
    routes = {
        "Kierowca 1": addresses[0::3],
        "Kierowca 2": addresses[1::3],
        "Kierowca 3": addresses[2::3],
    }
    return jsonify(routes)
if __name__ == "__main__":
    app.run()












Jot something down









