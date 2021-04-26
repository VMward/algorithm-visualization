from functools import lru_cache
import graphene
from fastapi import FastAPI
from starlette.graphql import GraphQLApp
from . import config
from fastapi.logger import logger
import logging
from ..algorithms import misc

gunicorn_logger = logging.getLogger('gunicorn.error')
logger.handlers = gunicorn_logger.handlers

@lru_cache()
def get_settings():
    return config.Settings()


class Query(graphene.ObjectType):
    isAnagram = graphene.String(s1=graphene.String(default_value="stranger"), s2=graphene.String(default_value="stranger"))
    def resolve_isAnagram(self, info, s1, s2):
        return misc.isAnagram(s1, s2)




app = FastAPI()
app.add_route("/graphql", GraphQLApp(schema=graphene.Schema(query=Query)))

if __name__ != "main":
    logger.setLevel(gunicorn_logger.level)
else:
    logger.setLevel(logging.DEBUG)