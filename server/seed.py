from app import app, db
from models import User, Entry

with app.app_context():
    User.query.delete()
    Entry.query.delete()
    
    
    user1 = User(username='alice', password='password123')
    user2 = User(username='bob', password='password456')
    db.session.add_all([user1, user2])
    db.session.commit()
    
    
    e1 = Entry(title='Alice\'s First Entry', content='This is Alice\'s first entry.', user_id=user1.id)
    e2 = Entry(title='Bob\'s First Entry', content='This is Bob\'s first entry.', user_id=user2.id)
    db.session.add_all([e1, e2])
    db.session.commit() 
    print("Database seeded successfully!")