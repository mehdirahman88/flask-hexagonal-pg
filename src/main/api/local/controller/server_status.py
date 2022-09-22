from flask import current_app as app
from flask_apispec import MethodResource, doc


class ServerStatus(MethodResource):
    @doc(tags=["local"], description="Get server health status")
    def get(self):
        app.logger.info("Health status request received")
        return {
            "server": f"{app.config.get('APPNAME')} v{app.config.get('VERSION')}",
            "status": "running",
        }, 200
