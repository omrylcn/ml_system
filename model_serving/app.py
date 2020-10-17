from flask import Flask
from api.config import get_logger,DevelopmentConfig
from api.controller import prediction_app

_logger = get_logger(logger_name=__name__)



flask_app=Flask("ml_api")
flask_app.config.from_object(DevelopmentConfig)
flask_app.register_blueprint(prediction_app)
_logger.debug('Application instance created')

if __name__ == "__main__":
    flask_app.run()

