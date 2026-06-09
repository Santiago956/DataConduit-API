from dependency_injector import containers, providers
from src.service import ServiceContainer


class ApplicationContainer(containers.DeclarativeContainer):
    services = providers.Container(ServiceContainer)
    
    @classmethod
    def wire_controllers(cls):
        container = cls()
        
        container.wire(modules=["src.controller.v1.quality_controller"])
        
        return container