# from flask import Flask, request, jsonify
# import sqlite3

# app = Flask(__name__)
# CORS(app)

# from flask_cors import CORS
# import sqlite3
from flask import Flask, request, jsonify, send_from_directory
from datetime import datetime
from datetime import datetime, timezone
from flask_cors import CORS
import sqlite3


app = Flask(__name__)
CORS(app)  # enable CORS


# @app.route('/api/logs', methods=['POST'])
# def log_data():
#     data = request.get_json()
#     temperature = data.get('temperature')
#     humidity = data.get('humidity')
#     timestamp = datetime.now().strftime("%Y-%m-%d %H:%M:%S") 
    
#     # Store to database
#     conn = sqlite3.connect('iot_data.db')
#     cursor = conn.cursor()
#     cursor.execute("INSERT INTO logs (temperature, humidity) VALUES (?, ?)", (temperature, humidity))
#     conn.commit()
#     conn.close()

#     return jsonify({"status": "success"}), 201


@app.route('/api/logs', methods=['POST'])
def log_data():
    data = request.get_json()
    temperature = data.get('temperature')
    humidity = data.get('humidity')

    # Always UTC with timezone info
    timestamp = datetime.now(timezone.utc).isoformat()

    conn = sqlite3.connect('iot_data.db')
    cursor = conn.cursor()
    cursor.execute(
        "INSERT INTO logs (temperature, humidity, timestamp) VALUES (?, ?, ?)",
        (temperature, humidity, timestamp)
    )
    conn.commit()
    conn.close()

    return jsonify({"status": "success"}), 201


# GET data endpoint
@app.route('/api/logs', methods=['GET'])
def get_logs():
    try:
        conn = sqlite3.connect('iot_data.db')
        conn.row_factory = sqlite3.Row  # Enable dictionary-like access
        cursor = conn.cursor()
        cursor.execute("SELECT * FROM logs ORDER BY timestamp DESC")
        rows = cursor.fetchall()
    finally:
        conn.close()

    logs = [
        {
            "id": row["id"],
            "temperature": row["temperature"],
            "humidity": row["humidity"],
            "timestamp": row["timestamp"]
        }
        for row in rows
    ]
    return jsonify(logs)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)

