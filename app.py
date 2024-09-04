import psycopg2

def connect():
    conn = psycopg2.connect(
        dbname="postgres",
        user="postgres",
        password="mysecretpassword", # про имя дб, пользователя и пароля рассказано в доке
        host="my_postgres" # тут мы указываем имя созданной сети в docker
    )
    return conn

def create_table(conn): # создание таблицы 
    with conn.cursor() as cur:
        cur.execute("""
            CREATE TABLE IF NOT EXISTS test (
                id SERIAL PRIMARY KEY,
                data TEXT NOT NULL
            )
        """)
        conn.commit()

def insert_data(conn, data): # вставка данных в таблицу
    with conn.cursor() as cur:
        cur.execute("INSERT INTO test (data) VALUES (%s) RETURNING id;", (data,))
        conn.commit()
        return cur.fetchone()[0]

def read_data(conn): # чтение данных из таблицы бд
    with conn.cursor() as cur:
        cur.execute("SELECT * FROM test;")
        rows = cur.fetchall()
        for row in rows:
            print(row)

if __name__ == '__main__':
    conn = connect()
    create_table(conn)
    new_id = insert_data(conn, 'Hello, Docker!')
    print(f'Data inserted with ID: {new_id}')
    read_data(conn)
    conn.close()