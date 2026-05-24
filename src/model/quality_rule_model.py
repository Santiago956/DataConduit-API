from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy import Column, String, Integer, Float, Boolean, JSON

from src.gateway.sqlite_client import SQLiteBase

class QualityRuleModel(SQLiteBase):
    __tablename__ = "quality_rule"
    __tableargs__ = (
        PrimaryKeyConstraint("id", name="pk_quality_rule"),
        UniqueConstraint("rule_type", "table_target", "column_target", name="unique_rule"),
    )
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    rule_type = Column(String, nullable=False)
    table_target = Column(String, nullable=False)
    column_target = Column(String, nullable=False)
    min_value = Column(Float)
    max_value = Column(Float)
    enum_value = Column(JSON) # ["A", "B", "C"]
    regex_expr = Column(String)
    is_active = Column(Boolean, nullable=False)