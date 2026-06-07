from sqlalchemy.exc import IntegrityError
from fastapi.encoders import jsonable_encoder
from pydantic import ValidationError

from src.service.interface.interface_quality_rule_service import IQualityRuleService
from src.repository.interface.interface_quality_rule_repository import IQualityRuleRepository
from src.model.quality_rule_model import QualityRuleModel
from src.exceptions.quality_rule_exceptions import (
    QualityRuleExists,
    QualityRuleNotFound,
    QualityRuleIsDeactivated,
    QualityRuleIsActive
    )
from src.exceptions.repo_exceptions import UpdateIsNotActive, RevertDeleteIsActive
from src.schema.quality_rule_schema import QualityRuleSchema



class QualityRuleService(IQualityRuleService):
    def __init__(self, quality_rule_repo: IQualityRuleRepository):
        self.quality_rule_repo = quality_rule_repo
        
    def create_rule(self,
                    rule_type: str,
                    target_table: str,
                    target_column: str,
                    min_value: float | None = None,
                    max_value: float | None = None,
                    enum_value: list[str] | None = None,
                    regex_expr: str | None = None) -> QualityRuleModel:
        
        try:
            # Tabela tem que existir
            # Coluna tem que existir
            # Implementar check utilizando repository específico para tabela e coluna
            rule = self.quality_rule_repo.create(
                rule_type=rule_type,
                target_table=target_table,
                target_column=target_column,
                min_value=min_value,
                max_value=max_value,
                enum_value=enum_value,
                regex_expr=regex_expr
                )
        except IntegrityError as error:
            raise QualityRuleExists(f"Rule with type '{rule_type}' for column '{target_column}' in table '{target_table}' already exists.") from error
        except Exception as error:
            raise error
        
        return rule

    def read_rule_by_id(self, rule_id: int) -> QualityRuleModel:
        try:
            rule = self.quality_rule_repo.read(rule_id)
        except Exception as error:
            raise error

        if not rule:
            raise QualityRuleNotFound(f"Rule {rule_id} not found.")

        return rule

    def read_rules_by_target_table(self, target_table: str, is_active: bool | None = True) -> list[QualityRuleModel]:
        try:
            rules = self.quality_rule_repo.read_by_target_table(target_table, is_active)
        except Exception as error:
            raise error

        return rules
    
    def update_rule(self, rule_id: int, new_rule_data: dict) -> QualityRuleModel:
        try:
            rule = self.quality_rule_repo.read(rule_id=rule_id)
            
            rule_dict = jsonable_encoder(rule)
            rule_dict.update({key: value for key, value in new_rule_data.items() if value is not None and key in ["target_table", "target_column", "rule_type"] and value is not None})
            QualityRuleSchema.model_validate(rule_dict)

            rule = self.quality_rule_repo.update(rule_id=rule_id,
                                                new_rule_data=new_rule_data)
            
            return rule

        except IntegrityError as error:
            raise QualityRuleExists(f"Rule with the same type and target column already exists.") from error
        except ValidationError as error:
            raise QualityRuleExists(f"Invalid rule data provided.") from error
        except UpdateIsNotActive:
            raise QualityRuleIsDeactivated(f"Cannot update rule {rule_id} because it is deactivated.")
        except Exception as error:
            raise error

    def deactivate_by_id(self, rule_id: int) -> QualityRuleModel:
        try:
            rule = self.quality_rule_repo.deactivate(rule_id=rule_id)
            if not rule:
                raise QualityRuleNotFound(f"Rule {rule_id} not found.")

            return rule
        except QualityRuleIsDeactivated:
            raise QualityRuleIsDeactivated(f"Rule {rule_id} is already deactivated.")
    
    def activate_by_id(self, rule_id: int) -> QualityRuleModel:
        try:
            rule = self.quality_rule_repo.activate(rule_id=rule_id)
            if not rule:
                raise QualityRuleNotFound(f"Rule {rule_id} not found.")
            
            return rule
        
        except RevertDeleteIsActive:
            raise QualityRuleIsActive(f"Rule {rule_id} is already active and cannot be reactivated.")