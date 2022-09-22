from flask import Blueprint
from flask_restful import Api

from src.main.api.local.controller.server_status import ServerStatus


blueprint = Blueprint("local", __name__)

api = Api(blueprint)
api.add_resource(ServerStatus, "/server/status")

__all__ = ["blueprint", "ServerStatus"]
