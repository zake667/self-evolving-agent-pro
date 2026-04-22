from flask import Flask, jsonify
import os

app = Flask(__name__)

@app.route('/')
def home():
    return jsonify({
        "status": "online",
        "message": "Welcome to the Self-Evolving Agent API",
        "version": "1.0.0"
    })

@app.route('/logs')
def get_logs():
    log_path = "docs/agent_activity.log"
    if os.path.exists(log_path):
        with open(log_path, "r") as f:
            lines = f.readlines()[-20:] # Devolvemos las últimas 20 líneas
        return jsonify({"logs": lines})
    return jsonify({"error": "Log file not found"}), 404

@app.route('/health')
def health():
    return jsonify({"status": "healthy"})

if __name__ == '__main__':
    print("🚀 API starting on http://127.0.0.1:5000")
    app.run(debug=True, port=5000)
