from src.main.config.development import DevelopmentConfig
from src.main.config.production import ProductionConfig


get_config = dict(
    development=DevelopmentConfig,
    preprod=ProductionConfig,
    production=ProductionConfig,
)
