from src.repository.interface.interface_quality_rule_repository import IQualityRuleRepository
from src.model.quality_rule_model import QualityRuleModel
from src.gateway.sqlite_client import SQLiteClient


class SQLiteQualityRuleRepository(IQualityRuleRepository):
    def __init__(self):
        self.sqlite_client = SQLiteClient()
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
               regex_pattern: str | None = None) -> QualityRuleModel:
        
        with self.sqlite_client()._get_session() as db_session:
            rule = QualityRuleModel(
                rule_type=rule_type,
                target_table=target_table,
                target_column=target_column,
                min_value=min_value,
                max_value=max_value,
                enum_value=enum_value,
                regex_pattern=regex_pattern,
                is_active = True
            )
            db_session.add(rule)
            db_session.commit()
            db_session.refresh(rule)
            return rule