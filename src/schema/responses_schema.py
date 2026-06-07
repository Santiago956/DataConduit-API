from typing import Optional

from src.schema.quality_rule_schema import QualityRuleSchema

class QualityRuleObjectResponse(QualityRuleSchema):
    id: int
    is_active: bool
    
    class Config:
        from_attributes = True