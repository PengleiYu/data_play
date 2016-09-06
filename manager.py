from app import create_app, db
import os
from flask_script import Manager, Server, Shell
from flask_migrate import Migrate, MigrateCommand
from app.models import Device, Sensor, Number

app = create_app(os.getenv('FLASK_CONFIG') or 'default')
manager = Manager(app=app)
server = Server(host='0.0.0.0')
migrate = Migrate(app=app, db=db)

manager.add_command('run', server)
manager.add_command('db', MigrateCommand)


def make_shell_context():
    return dict(app=app, db=db, Device=Device, Sensor=Sensor, Number=Number)


manager.add_command('shell', Shell(make_context=make_shell_context))

if __name__ == '__main__':
    manager.run()
