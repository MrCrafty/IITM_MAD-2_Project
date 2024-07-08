from website import create_app
from flask_restful import Api
from website.api import initialize_api
from website.auth import initialize_auth


if (__name__ == "__main__"):
    app = create_app()
    api = Api(app)
    initialize_api(api)
    initialize_auth(api)
    app.run(host="0.0.0.0", port=8000, debug=True)
