import sys
from pathlib import Path
sys.path.insert(0, str(Path(__file__).resolve().parents[1]))
from src.schema.responses_schema import QualityRuleObjectResponse
from src.model.quality_rule_model import QualityRuleModel

r = QualityRuleModel()
r.id = 1
r.rule_type = 'unicity'
r.target_table = 't'
r.target_column = 'c'
r.min_value = None
r.max_value = None
r.enum_value = None
r.regex_expr = None
r.is_active = True

print(QualityRuleObjectResponse.model_validate(r))
