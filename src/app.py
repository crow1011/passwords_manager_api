import connexion

app = connexion.FlaskApp(__name__, specification_dir='openapi/')
app.add_api('passwords_manager.openapi.yaml')
app.run(port=8080)