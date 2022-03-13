import connexion

def create_app() -> connexion.FlaskApp:
    """ Create Connexion Flask app """
    app = connexion.FlaskApp(__name__, specification_dir='openapi/')
    app.add_api('passwords_manager.openapi.yaml')

    return app

if __name__ == "__main__":
    app = create_app()
    app.run(port=8080)