from app.models import User, Post
from app.db import Session, Base, engine

# drop and rebuild tables
Base.metadata.drop_all(engine)
Base.metadata.create_all(engine)

db = Session()

# insert users
db.add_all([
    User(username='cjohnson74', email='cjohnson74.tech@gmail.com', password='password1'),
    User(username='genesis305', email='genesis305vw@gmail.com', password='password12'),
    User(username='hendrix1', email='hendrix1@gmail.com', password='password123'),
    User(username='jaxx2', email='jaxx2@gmail.com', password='password1234'),
    User(username='lana3', email='lana3@gmail.com', password='password12345'),
])

db.commit()

db.close()