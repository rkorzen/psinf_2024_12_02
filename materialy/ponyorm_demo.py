from pony.orm import Database, Required, Set, db_session, select

# Tworzenie połączenia z bazą danych SQLite
db = Database()
db.bind(provider='sqlite', filename='pony_example.db', create_db=True)

# Definiowanie tabeli User
class User(db.Entity):
    name = Required(str)
    email = Required(str, unique=True)
    posts = Set('Post')

# Definiowanie tabeli Post
class Post(db.Entity):
    title = Required(str)
    user = Required(User)

# Generowanie tabel w bazie danych
db.generate_mapping(create_tables=True)

# Funkcja pokazująca operacje CRUD
@db_session
def run_demo():
    # Tworzenie użytkownika
    user = User(name="Rafał Korzeniewski", email="rafal@example.com")
    print(f"Added user: {user}")

    # Dodawanie postów
    post1 = Post(title="My First Post", user=user)
    post2 = Post(title="My Second Post", user=user)
    print(f"Added posts: {[post1, post2]}")

    # Pobieranie użytkownika i jego postów
    retrieved_user = User.get(name="Rafał Korzeniewski")
    print(f"Retrieved user: {retrieved_user.name}, email: {retrieved_user.email}")
    for post in retrieved_user.posts:
        print(f"Post title: {post.title}")

    # Aktualizacja emaila użytkownika
    retrieved_user.email = "new_email@example.com"
    print(f"Updated user email: {retrieved_user.email}")

    # Usuwanie postu
    post1.delete()
    print(f"Deleted post: {post1.title}")

    # Usuwanie użytkownika
    retrieved_user.delete()
    print(f"Deleted user: {retrieved_user.name}")

# Uruchomienie przykładu
if __name__ == "__main__":
    run_demo()
