from src.main.config.base import BaseConfig


class DevelopmentConfig(BaseConfig):
    """Basic default configurations for development instance"""

    """APISPEC_SWAGGER_URL: URL for swagger.json file. Key is related to apispec library.

    Set None to disable serving this resource.
    """
    APISPEC_SWAGGER_URL = "/api/apispec/spec"

    """APISPEC_SWAGGER_UI_URL: URL for swagger-ui. Key is related to apispec library.

    Set None to disable serving this view.
    """
    APISPEC_SWAGGER_UI_URL = "/api/apispec/ui"
