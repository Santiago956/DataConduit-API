from dependency_injector import containers, providers
from src.gateway.sqlite_client import SQLiteClient


class GatewayContainer(containers.DeclarativeContainer):
    sqlite_client = providers.Singleton(SQLiteClient)