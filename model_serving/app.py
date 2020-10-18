from flask import Flask
from api.config import get_logger,DevelopmentConfig
from api.controller import prediction_app


_logger = get_logger(logger_name=__name__)

config_app=DevelopmentConfig()
flask_app=Flask("ml_api")
flask_app.register_blueprint(prediction_app)
_logger.debug('Application instance created')


if __name__ == "__main__":
    flask_app.run(**config_app.dict())

