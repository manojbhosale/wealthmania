from app import wealthApp, db
from app.models import User, Security


@app.shell_context_processor
def make_shell_context():
    return {'db': db, 'User': User, 'Security':Security}


