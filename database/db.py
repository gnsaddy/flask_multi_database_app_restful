from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()


def initialize_db(app):
    db.init_app(app)

    with app.app_context():
        db.create_all()
        db.create_all(bind=['users'])
        db.create_all(bind=['items'])
