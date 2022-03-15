import connexion
from flask_mongoengine import MongoEngine

from tools.error_handlers import conflict_handler, not_found_handler
from tools.exceptions import ConflictException, NotFoundException

# will move to env
default_config = {'MONGODB_SETTINGS': {
    'db': 'test_db',
    'host': 'SET_ME',
    'port': 27017,
    'username': 'admin',
    'password': 'password',
    'authentication_source': 'admin'}}


def create_app(config: dict = None) -> connexion.FlaskApp:
    """ Create Connexion Flask app """
    connexion_app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    connexion_app.add_api('passwords_manager.openapi.yaml')
    config = default_config if config is None else config
    connexion_app.app.config.update(config)
    db = MongoEngine(app=connexion_app.app)
    connexion_app.add_error_handler(NotFoundException, not_found_handler)
    connexion_app.add_error_handler(ConflictException, conflict_handler)
    return connexion_app


if __name__ == "__main__":
    app = create_app()
    app.run(port=8080, debug=True)
