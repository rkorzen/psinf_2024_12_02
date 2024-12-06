from sqlalchemy import create_engine, Column, Integer, String, ForeignKey

from sqlalchemy.orm import sessionmaker, relationship, declarative_base

# Tworzenie bazy danych SQLite
engine = create_engine('sqlite:///example.db', echo=True)

# Deklaracja bazy
Base = declarative_base()

# Definicja tabeli User
class User(Base):
    __tablename__ = 'users'

    id = Column(Integer, primary_key=True)
    name = Column(String, nullable=False)
    email = Column(String, unique=True)
    posts = relationship("Post", back_populates="user")

# Definicja tabeli Post (relacja One-to-Many z User)
class Post(Base):
    __tablename__ = 'posts'

    id = Column(Integer, primary_key=True)
    title = Column(String, nullable=False)
    user_id = Column(Integer, ForeignKey('users.id'))
    user = relationship("User", back_populates="posts")

# Tworzenie tabel w bazie danych
Base.metadata.create_all(engine)

# Konfiguracja sesji
Session = sessionmaker(bind=engine)
session = Session()

# Funkcja pokazująca operacje CRUD
def run_demo():
    # Tworzenie użytkownika
    user = User(name="Rafał Korzeniewski", email="rafal@example.com")
    session.add(user)
    session.commit()

    print(f"Added user: {user}")
    print()
    # Dodawanie postów
    post1 = Post(title="My First Post", user=user)
    post2 = Post(title="My Second Post", user=user)
    session.add_all([post1, post2])
    session.commit()
    print(f"Added posts: {[post1, post2]}")
    print()

    # Pobieranie użytkownika i jego postów
    retrieved_user = session.query(User).filter_by(name="Rafał Korzeniewski").first()
    print(f"Retrieved user: {retrieved_user.name}, email: {retrieved_user.email}")
    for post in retrieved_user.posts:
        print(f"Post title: {post.title}")

    print()
    
    # Aktualizacja emaila użytkownika
    retrieved_user.email = "new_email@example.com"
    session.commit()
    print(f"Updated user email: {retrieved_user.email}")
    print()

    # Usuwanie postu
    session.delete(post1)
    session.commit()
    print(f"Deleted post: {post1.title}")
    print()

    # Usuwanie użytkownika
    session.delete(retrieved_user)
    session.commit()
    print(f"Deleted user: {retrieved_user.name}")
    print()
    
# Uruchomienie przykładu
if __name__ == "__main__":
    run_demo()

    # Zamknięcie sesji
    session.close()
