from sqlalchemy import PrimaryKeyConstraint, UniqueConstraint
from sqlalchemy import Column, String, Integer, Float, Boolean, JSON

from src.gateway.sqlite_client import SQLiteBase

class QualityRuleModel(SQLiteBase):
    __tablename__ = "quality_rule"
    __tableargs__ = (
        PrimaryKeyConstraint("id", name="pk_quality_rule"),
        UniqueConstraint("rule_type", "target_table", "target_column", name="unique_rule"),
    )
    
    id = Column(Integer, primary_key=True, autoincrement=True)
    rule_type = Column(String, nullable=False)
    target_table = Column(String, nullable=False)
    target_column = Column(String, nullable=False)
    min_value = Column(Float)
    max_value = Column(Float)
    enum_value = Column(JSON) # ["A", "B", "C"]
    regex_expr = Column(String)
    is_active = Column(Boolean, nullable=False)
    
    def __repr__(self):
        return f"""<QualityRuleModel(
            id={self.id}, 
            rule_type='{self.rule_type}',
            target_table='{self.target_table}',
            target_column='{self.target_column}',
            min_value={self.min_value},
            max_value={self.max_value},
            enum_value={self.enum_value},
            regex_expr='{self.regex_expr}',
            is_active={self.is_active}
            )>"""