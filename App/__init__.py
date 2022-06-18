from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy

# init SQLAlchemy so we can use it later in our models
db = SQLAlchemy()
# handler = RotatingFileHandler('app.log', maxBytes=100000, backupCount=3)
# logger = logging.getLogger('tdm')
# logger.setLevel(logging.ERROR)
# logger.addHandler(handler)

def create_app():
    app = Flask(__name__)

    app.config['SECRET_KEY'] = 'secret-key-goes-here'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:root@localhost:13306/dirty_documents'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'jdbc:postgresql://localhost:5432/dirty_documents'
    #app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@localhost:5432/dirty_documents'
    app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:postgres@postgres:5432/dirty_documents'

    db.init_app(app)

    login_manager = LoginManager()
    login_manager.login_view = 'auth.login'
    login_manager.init_app(app)

    from .entities import User

    @login_manager.user_loader
    def load_user(user_id):
        return User.query.get(int(user_id))

    # blueprint for auth routes in our app
    from .auth import auth as auth_blueprint
    app.register_blueprint(auth_blueprint)

    from .main import main as main_blueprint
    app.register_blueprint(main_blueprint)

    return app


db.create_all(app=create_app())
