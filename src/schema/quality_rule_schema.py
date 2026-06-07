from pydantic import BaseModel, model_validator
from typing import Optional
from enum import Enum
import re

class RuleTypeEnum(str, Enum):
    unicity = "unicity"
    precision = "precision"
    validity = "validity"
    completeness = "completeness"

class QualityRuleSchema(BaseModel):
    rule_type: RuleTypeEnum
    target_table: str
    target_column: str
    min_value: Optional[float] = None
    max_value: Optional[float] = None
    enum_value: Optional[list[str]] = None
    regex_expr: Optional[str] = None
    
    @property
    def provided_params(self) -> set[str]:
        """Returns the set of provided parameters for the quality rule."""
        return {
            name
            for name, value in {
                "min_value": self.min_value,
                "max_value": self.max_value,
                "enum_value": self.enum_value,
                "regex_expr": self.regex_expr
            }.items()
            if value is not None
        }
    
    @classmethod
    def _check_simple_rule(cls, instance):
        if instance.provided_params:
            raise ValueError(f"Rule type '{instance.rule_type.value}' should not have any parameters, but the following were provided: {instance.provided_params}")
      
    @classmethod
    def _validate_regex(cls, pattern: str):
        try:
            re.compile(pattern)
        except re.error as e:
            raise ValueError(f"Invalid regex pattern: {pattern}. Error: {str(e)}")  
        
    @classmethod
    def _check_precision(cls, instance: "QualityRuleSchema"):
        params = instance.provided_params
        if params in ({"min_value", "max_value"}, {"enum_value"}):
            return
        raise ValueError(f"Rule type '{instance.rule_type.value}' should have either 'min_value' and 'max_value' or 'enum_value' parameters, but the following were provided: {params}")
    
    @classmethod
    def _check_validity(cls, instance: "QualityRuleSchema"):
        if instance.provided_params != {"regex_expr"}:
            raise ValueError(f"Rule type '{instance.rule_type.value}' should have 'regex_expr' parameter, but the following were provided: {instance.provided_params}")
        cls._validate_regex(instance.regex_expr)
    
    
    @model_validator(mode="after")
    def check_rule_params(self):
        match self.rule_type:
            case RuleTypeEnum.precision:
                self._check_precision(self)
            case RuleTypeEnum.validity:
                self._check_validity(self)
            case RuleTypeEnum.completeness:
                self._check_simple_rule(self)
            case RuleTypeEnum.unicity:
                self._check_simple_rule(self)
        return self
                
        

if __name__ == "__main__":
    QualityRuleSchema(
        rule_type="unicity",
        target_table="test",
        target_column="columnA",
    )
    

    