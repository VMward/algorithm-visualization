from functools import lru_cache
import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from . import config
from fastapi.logger import logger
import logging

gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers

@lru_cache()
def get_settings():
    return config.Settings()


class Query(graphene.ObjectType):
    hello = graphene.String(name=graphene.String(default_value="stranger"))
    def resolve_hello(self, info, name):
        return "Hello " + name


app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))

if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)