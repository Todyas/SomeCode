import psycopg2

# Параметры подключения к базе данных
conn = psycopg2.connect(
    dbname="testdb",
    user="postgres",
    password="123321",
    host="localhost",
    port="5432"
)

# Создание курсора для выполнения SQL-запросов
cur = conn.cursor()

# Создание таблицы (если она еще не создана)
cur.execute('''
    CREATE TABLE IF NOT EXISTS users (
        id SERIAL PRIMARY KEY,
        name VARCHAR(100),
        email VARCHAR(100)
    )
''')

# Вставка данных в таблицу
cur.execute('''
    INSERT INTO users (name, email) VALUES (%s, %s)
''', ("John Doe", "john.doe@example.com"))

# Коммит транзакции
conn.commit()

# Извлечение данных из таблицы
cur.execute('SELECT * FROM users')
rows = cur.fetchall()

for row in rows:
    print(row)

# Закрытие курсора и соединения
cur.close()
conn.close()
