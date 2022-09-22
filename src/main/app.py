from apispec import APISpec
from apispec.ext.marshmallow import MarshmallowPlugin
from flask import Flask
from flask_apispec import FlaskApiSpec
from flask_cors import CORS

from src.main.api import local
from src.main.config import get_config


def create_app(app_name: str, instance_name: str = None, instance_path: str = None):
    assert instance_name, f"instance_name must be provided"

    _initialize_logging()

    app = Flask(app_name)  # TODO: If instance folder is needed
    config = get_config[instance_name]
    app.config.from_object(config)

    _register_blueprints(app)
    _register_extensions(app)
    if app.debug:
        _register_apispec(app)

    return app


def _initialize_logging(**kwargs):
    """Initializes logging. Called before application initialization."""
    # TODO: User Your Logging Pattern
    pass


def _register_extensions(app: Flask):
    """Registers extensions with app config"""
    CORS(app)


def _register_blueprints(app: Flask):
    """Registers blueprints with URL prefixes"""
    app.register_blueprint(local.blueprint, url_prefix="/api/local")


def _register_apispec(app: Flask):
    """Registers apispec and resources for swagger. Must be called after registering blueprints"""
    app.config.update(
        {
            "APISPEC_SPEC": APISpec(
                title=app.config.get("APPNAME"),
                version=app.config.get("VERSION"),
                plugins=[MarshmallowPlugin()],
                openapi_version="2.0.0",
            ),
            # URL configs are in BaseConfig
            "JSON_SORT_KEYS": False,
        }
    )
    apispec = FlaskApiSpec()  # or, apispec.init_app(app)
    apispec.init_app(app)
    apispec.register(local.ServerStatus, blueprint=local.blueprint.name)
