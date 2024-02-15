from website import create_app
from flask_restful import Api
from website.api import initialize_route


if (__name__ == "__main__"):
    app = create_app()
    api = Api(app)
    initialize_route(api)
    app.run(host="0.0.0.0", port=8000, debug=True)
