from dependency_injector import containers, providers
from src.service.quality_rule_service import QualityRuleService
from src.service.interface.interface_quality_rule_service import IQualityRuleService
from src.repository import RepositoryContainer


class ServiceContainer(containers.DeclarativeContainer):
    repositories = providers.Container(RepositoryContainer)
    
    quality_rule_service: IQualityRuleService = providers.Factory(
        QualityRuleService,
        quality_rule_repo=repositories.quality_rule_repository
    )