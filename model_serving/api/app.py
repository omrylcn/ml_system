from flask import Flask
from config import get_logger,DevelopmentConfig
from controller import prediction_app

_logger = get_logger(logger_name=__name__)


application_config = create_app(config_object=DevelopmentConfig)

flask_app=Flask("ml_api")
flask_app.config.from_object(application_config)
flask_app.register_blueprint(prediction_app)
_logger.debug('Application instance created')

if __name__ == "__main__":
    flask_app.run()

