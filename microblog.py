from app import app, db
from app.models import Car, Post

@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'Car': Car, 'Post': Post}