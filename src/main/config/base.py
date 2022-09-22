from src.main import APPNAME, VERSION


class BaseConfig:
    """Basic default configurations"""

    APPNAME = APPNAME

    VERSION = VERSION

    """PROPAGATE_EXCEPTIONS: Flag to bypass FR error handlers for custom exceptions.
    
    Set this to False if you want to use FR error handlers instead.
    """
    PROPAGATE_EXCEPTIONS = True
