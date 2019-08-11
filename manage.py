from flask_migrate import MigrateCommand, Migrate
from flask_script import Manager


from app import create_app
from app.models import Number, User, db

app = create_app()
db.init_app(app)
db.create_all()

manager = Manager(app)
manager.add_command('db', MigrateCommand)
migrate = Migrate(app, db)

if __name__ == '__main__':
    manager.run()
