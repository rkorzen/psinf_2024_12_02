import psycopg2
from psycopg2 import sql

# Połączenie z PostgreSQL (do głównej bazy, np. 'postgres')
connection = psycopg2.connect(
    dbname="postgres",
    user="postgres",
    password="postgres",
    host="localhost",
    port=5432
)

connection.autocommit = True  # Włączenie trybu autocommit (tworzenie bazy wymaga tego trybu)
cursor = connection.cursor()

# Tworzenie bazy danych
try:
    cursor.execute(sql.SQL("CREATE DATABASE {}").format(sql.Identifier("xyz")))
    print("Baza danych 'xyz' została utworzona.")
except psycopg2.Error as e:
    print(f"Błąd podczas tworzenia bazy danych: {e}")

# Zamknięcie połączenia
cursor.close()
connection.close()
