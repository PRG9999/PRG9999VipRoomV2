from flask import Flask, request, jsonify
from datetime import datetime
from flask_cors import CORS

app = Flask(__name__)
CORS(app)  # Biar bisa diakses dari HTML GitHub Pages

@app.route("/")
def home():
    return "🟢 Server PRG9999 aktif."

@app.route("/api/status", methods=["POST"])
def receive_status():
    data = request.get_json()
    action = data.get("action")
    content = data.get("data")

    print(f"[{datetime.now()}] Aksi: {action} | Data: {content}")
    
    return jsonify({
        "success": True,
        "message": f"Aksi '{action}' diterima."
    })

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=3000)
