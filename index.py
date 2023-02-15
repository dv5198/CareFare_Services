import os
import typing
import strawberry
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from strawberry.asgi import GraphQL
from strawberry.permission import BasePermission
from fastapi.responses import HTMLResponse
from starlette.requests import Request
from starlette.websockets import WebSocket
from strawberry.types import Info
from strawberry.file_uploads import Upload

from models.category import Category
import category

@strawberry.type
class Query:
    @strawberry.field(permission_classes=[])
    def category(self) -> typing.List[Category]:
       return category.get_category()
    
@strawberry.type
class Mutation:
    @strawberry.field
    def add_category(self, name: str) -> str:
        pass
    
schema = strawberry.Schema(query=Query, mutation=Mutation)

graphql_schema = strawberry.Schema(query=Query, mutation=Mutation)
if os.getenv("DEBUG", "False") == "True":
    graphql_app = GraphQL(graphql_schema)
else:
    graphql_app = GraphQL(graphql_schema, graphiql=True, debug=False)

app = FastAPI(title="carefare services")
app.add_route("/graphql", graphql_app)