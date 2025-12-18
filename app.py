from flask import Flask
from flask_restful import Api
from config import Config
import models.models as models
import routes.routes as routes


def create_app():
    app = Flask(__name__)
    app.config.from_object(Config)

    # initialize extensions
    models.db.init_app(app)

    api = Api(app)
    routes.register_routes(api)

    with app.app_context():
        models.db.create_all()

    return app


if __name__ == '__main__':
    app = create_app()
    app.run(debug=True, host='0.0.0.0', port=5000)
