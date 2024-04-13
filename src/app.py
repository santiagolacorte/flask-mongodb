# Utilitary imports
from flask import Flask, render_template

# Local imports
from .config.mongodb import db_config, mongo
from .routes.employees import employees


# Instanciate the app
app = Flask(__name__)


# Set the URI for the database
app.config["MONGO_URI"] = "mongodb://{username}:{password}@mongo/{db}".format(**db_config)

# Connect to the database
mongo.init_app(app)

# Blueprint for the '/employees' endpoint
app.register_blueprint(employees, url_prefix='/employees')


@app.route('/')
def index() -> str:
    """Render the 'index.html' template."""

    return render_template('index.html')


@app.errorhandler(404)
def not_found(error) -> str:
    """Error handler for the 404 status code."""

    # Loggin the error
    app.logger.error(f"Error 404: {error}")

    return render_template('pages/404.html'), 404


# Execute the Flask app
if __name__ == '__main__':
    app.run(debug=True)
