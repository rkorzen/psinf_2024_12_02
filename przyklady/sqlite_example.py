import sqlite3

# Włączanie obsługi kluczy obcych
def enable_foreign_keys(connection):
    connection.execute("PRAGMA foreign_keys = ON")

# Tworzenie bazy danych i tabel
def create_tables(connection):
    cursor = connection.cursor()

    # Tworzenie tabeli użytkowników
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS users (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        name TEXT NOT NULL,
        email TEXT NOT NULL UNIQUE
    )
    """)

    # Tworzenie tabeli zamówień
    cursor.execute("""
    CREATE TABLE IF NOT EXISTS orders (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        user_id INTEGER NOT NULL,
        product_name TEXT NOT NULL,
        amount INTEGER NOT NULL,
        FOREIGN KEY (user_id) REFERENCES users (id) ON DELETE CASCADE
    )
    """)

    connection.commit()
    print("Tabele zostały utworzone.")

# Wstawianie użytkownika
def insert_user(connection, name, email):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO users (name, email) VALUES (?, ?)", (name, email))
        connection.commit()
        print(f"Użytkownik {name} został dodany.")
    except sqlite3.IntegrityError as e:
        print(f"Błąd: {e}")

# Wstawianie zamówienia
def insert_order(connection, user_id, product_name, amount):
    cursor = connection.cursor()
    try:
        cursor.execute("INSERT INTO orders (user_id, product_name, amount) VALUES (?, ?, ?)", 
                       (user_id, product_name, amount))
        connection.commit()
        print(f"Zamówienie '{product_name}' zostało dodane.")
    except sqlite3.IntegrityError as e:
        print(f"Błąd: {e}")

# Pobieranie wszystkich użytkowników
def get_all_users(connection):
    cursor = connection.cursor()
    cursor.execute("SELECT * FROM users")
    users = cursor.fetchall()
    print("Użytkownicy:")
    for user in users:
        print(user)

# Pobieranie zamówień użytkownika
def get_user_orders(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("""
    SELECT orders.id, orders.product_name, orders.amount
    FROM orders
    WHERE orders.user_id = ?
    """, (user_id,))
    orders = cursor.fetchall()
    print(f"Zamówienia użytkownika {user_id}:")
    for order in orders:
        print(order)

# Pobieranie wszystkich zamówień z danymi użytkowników
def get_all_orders_with_users(connection):
    cursor = connection.cursor()
    cursor.execute("""
    SELECT users.name, users.email, orders.product_name, orders.amount
    FROM users
    JOIN orders ON users.id = orders.user_id
    """)
    results = cursor.fetchall()
    print("Wszystkie zamówienia z danymi użytkowników:")
    for result in results:
        print(result)

# Usuwanie użytkownika (z klauzulą ON DELETE CASCADE)
def delete_user(connection, user_id):
    cursor = connection.cursor()
    cursor.execute("DELETE FROM users WHERE id = ?", (user_id,))
    connection.commit()
    print(f"Użytkownik o ID {user_id} został usunięty.")

# Główna funkcja
def main():
    # Połączenie z bazą danych
    connection = sqlite3.connect("example_complete.db")
    enable_foreign_keys(connection)

    # Tworzenie tabel
    create_tables(connection)

    # Dodawanie użytkowników
    insert_user(connection, "Alice", "alice@example.com")
    insert_user(connection, "Bob", "bob@example.com")

    # Pobieranie wszystkich użytkowników
    get_all_users(connection)

    # Pobieranie ID użytkowników
    cursor = connection.cursor()
    cursor.execute("SELECT id FROM users WHERE name = ?", ("Alice",))
    alice_id = cursor.fetchone()[0]

    cursor.execute("SELECT id FROM users WHERE name = ?", ("Bob",))
    bob_id = cursor.fetchone()[0]

    # Dodawanie zamówień
    insert_order(connection, alice_id, "Laptop", 1)
    insert_order(connection, alice_id, "Mouse", 2)
    insert_order(connection, bob_id, "Keyboard", 1)

    # Pobieranie zamówień dla użytkownika Alice
    get_user_orders(connection, alice_id)

    # Pobieranie wszystkich zamówień z danymi użytkowników
    get_all_orders_with_users(connection)

    # Usuwanie użytkownika i sprawdzanie efektów (ON DELETE CASCADE)
    delete_user(connection, alice_id)
    get_all_orders_with_users(connection)

    # Zamknięcie połączenia
    connection.close()

if __name__ == "__main__":
    main()
