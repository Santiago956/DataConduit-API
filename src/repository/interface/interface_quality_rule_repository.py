from abc import ABC, abstractmethod

from src.model.quality_rule_model import QualityRuleModel

class IQualityRuleRepository(ABC):
    """
    Interface for QualityRuleRepository, defining the contract for CRUD operations on quality rules."""
    
    @abstractmethod
    def create(self,
               rule_type: str,
               target_table: str,
               target_column: str,
               min_value: float | None = None,
               max_value: float | None = None,
               enum_value: list[str] | None = None,
               regex_expr: str | None = None) -> QualityRuleModel:
        """
        Create a new quality rule with the specified parameters.
        """
        
        pass
    
    @abstractmethod
    def read(self,
             rule_id: int) -> QualityRuleModel | None:
        """"
        Read a quality rule by its ID.
        """
        pass
    
    @abstractmethod
    def read_by_target_table(self,
                             target_table: str,
                             is_active: bool | None = True) -> list[QualityRuleModel]:
        """"
        Read quality rules by their target table.
        """
        pass
    
    @abstractmethod
    def update(self,
               rule_id: int,
               new_rule_data: dict) -> QualityRuleModel:
        """"
        Update a quality rule with the specified parameters.
        """
        pass
    
    @abstractmethod
    def delete(self,
               rule_id: int) -> QualityRuleModel:
        """"
        Delete a quality rule by its ID.
        """
        pass
    
    @abstractmethod
    def revert_delete(self,
               rule_id: int) -> QualityRuleModel:
        """"
        Revert the deletion of a quality rule by its ID.
        """
        pass