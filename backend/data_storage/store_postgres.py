import psycopg2

def connect_to_postgresql():
    conn = psycopg2.connect(
        database="sentiment_db",
        user="user",
        password="password",
        host="localhost",
        port="5432",
        sslmode='require'
    )
    return conn

def store_processed_data_in_postgresql(data):
    conn = connect_to_postgresql()
    cursor = conn.cursor()
    for item in data:
        cursor.execute("INSERT INTO sentiment_data (text, sentiment) VALUES (%s, %s)", (item['text'], item['sentiment']))
    conn.commit()
    cursor.close()
    conn.close()
