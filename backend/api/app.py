from flask import Flask, jsonify
from flask_cors import CORS
import psycopg2

app = Flask(__name__)
CORS(app)

def get_sentiment_data():
    conn = psycopg2.connect(
        database="sentiment_db",
        user="user",
        password="password",
        host="localhost",
        port="5432"
    )
    cursor = conn.cursor()
    cursor.execute("SELECT * FROM sentiment_data")
    data = cursor.fetchall()
    conn.close()
    return data

@app.route('/api/sentiments', methods=['GET'])
def sentiments():
    data = get_sentiment_data()
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
