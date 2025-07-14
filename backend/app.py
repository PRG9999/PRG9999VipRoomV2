from flask import Flask, request, jsonify
from flask_cors import CORS
import socket

app = Flask(__name__)
CORS(app)  # Izinkan akses dari luar (GitHub Pages)

# Simulasi data server bot
bots = {
    "B1": {"status": "active", "ip": "192.168.1.101", "lag": False},
    "B2": {"status": "active", "ip": "192.168.1.102", "lag": False},
    "B3": {"status": "inactive", "ip": "192.168.1.103", "lag": False},
}

@app.route("/api/bots", methods=["GET"])
def get_bots():
    return jsonify(bots)

@app.route("/api/bots/<bot_id>/toggle", methods=["POST"])
def toggle_bot(bot_id):
    if bot_id in bots:
        current = bots[bot_id]["status"]
        bots[bot_id]["status"] = "inactive" if current == "active" else "active"
        return jsonify({"success": True, "status": bots[bot_id]["status"]})
    return jsonify({"success": False}), 404

@app.route("/api/bots/<bot_id>/lag", methods=["POST"])
def toggle_lag(bot_id):
    if bot_id in bots:
        bots[bot_id]["lag"] = not bots[bot_id]["lag"]
        return jsonify({"success": True, "lag": bots[bot_id]["lag"]})
    return jsonify({"success": False}), 404

if __name__ == "__main__":
    # Ambil IP lokal HP secara otomatis
    hostname = socket.gethostname()
    local_ip = socket.gethostbyname(hostname)
    print(f"🔗 Server Flask aktif di http://{local_ip}:3000")
    app.run(host=local_ip, port=3000)
