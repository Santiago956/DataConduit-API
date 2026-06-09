from src.repository.interface.interface_quality_rule_repository import IQualityRuleRepository
from src.model.quality_rule_model import QualityRuleModel
from src.gateway.sqlite_client import SQLiteClient
from src.exceptions.repo_exceptions import RevertDeleteIsActive, DeleteIsNotActive, UpdateIsNotActive

class SQLiteQualityRuleRepository(IQualityRuleRepository):
    def __init__(self, sqlite_client: SQLiteClient):
        self.sqlite_client = sqlite_client
    """
    SQLite implementation of the IQualityRuleRepository interface, providing CRUD operations for quality rules using SQLite as the database.
    """
    def create(self,
               rule_type: str,
               target_table: str,
               target_column: str,
               min_value: float | None = None,
               max_value: float | None = None,
               enum_value: list[str] | None = None,
               regex_expr: str | None = None) -> QualityRuleModel:
        
        with self.sqlite_client._get_session() as db_session:
            rule = QualityRuleModel(
                rule_type=rule_type,
                target_table=target_table,
                target_column=target_column,
                min_value=min_value,
                max_value=max_value,
                enum_value=enum_value,
                regex_expr=regex_expr,
                is_active = True
            )
            db_session.add(rule)
            db_session.commit()
            db_session.refresh(rule)
            
            return rule
        
    def read(self,
             rule_id: int) -> QualityRuleModel | None:
        
        with self.sqlite_client._get_session() as db_session:
            rule = (
                db_session.query(QualityRuleModel)
                .filter(QualityRuleModel.id == rule_id)
                .first()
            )
            
            return rule
        
    def read_by_target_table(self,
                             target_table: str,
                             is_active: bool | None = True) -> list[QualityRuleModel]:
        
        with self.sqlite_client._get_session() as db_session:
            query = db_session.query(QualityRuleModel)
            if is_active is not None:
                query = query.filter(QualityRuleModel.target_table == target_table,
                                     QualityRuleModel.is_active == is_active)
            else:
                query = query.filter(QualityRuleModel.target_table == target_table).all()
            
            return query.all()

    def update(self,
               rule_id: int,
               new_rule_data: dict) -> QualityRuleModel:
        
        with self.sqlite_client._get_session() as db_session:
            query = (
                    db_session
                    .query(QualityRuleModel)
                    .filter(QualityRuleModel.id == rule_id)
                )
            
            rule = query.first()
            
            if rule is None:
                raise ValueError(f"Quality rule with ID {rule_id} not found.")
            
            if not rule.is_active:
                raise UpdateIsNotActive(f"Cannot update an inactive quality rule with ID {rule_id}.")

            query.update(
                {key: value for key, value in new_rule_data.items() if key != "is_active"}
            )
            db_session.commit()
            rule = query.first()
            
            return rule
            
    def delete(self,
               rule_id: int) -> QualityRuleModel:
        
        with self.sqlite_client._get_session() as db_session:
            query = (
                db_session.query(QualityRuleModel)
                .filter(QualityRuleModel.id == rule_id)
            )
            rule = query.first()
            
            if rule is None:
                raise Exception(f"Quality rule with ID {rule_id} not found.")
            if not rule.is_active:
                raise DeleteIsNotActive(f"Quality rule with ID {rule_id} is not active and cannot be deleted.")
            
            query.update({"is_active": False})
            db_session.commit()
            rule = query.first()
            
            return rule
            
    def revert_delete(self,
               rule_id: int) -> QualityRuleModel:
        
        with self.sqlite_client._get_session() as db_session:
            query = (
                db_session.query(QualityRuleModel)
                .filter(QualityRuleModel.id == rule_id)
            )
            rule = query.first()
            
            if rule is None:
                raise Exception(f"Quality rule with ID {rule_id} not found.")
            if rule.is_active:
                raise RevertDeleteIsActive(f"Quality rule with ID {rule_id} is already active and cannot be reverted.")
            
            query.update({"is_active": True})
            db_session.commit()
            rule = query.first()
            
            return rule