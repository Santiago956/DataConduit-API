from dependency_injector import containers, providers
from src.repository.sqlite_quality_rule_repository import SQLiteQualityRuleRepository
from src.repository.interface.interface_quality_rule_repository import IQualityRuleRepository
from src.gateway import GatewayContainer

class RepositoryContainer(containers.DeclarativeContainer):
    gateway = providers.Container(GatewayContainer)
    
    quality_rule_repository: IQualityRuleRepository = providers.Factory(
        SQLiteQualityRuleRepository,
        sqlite_client=gateway.sqlite_client
        )