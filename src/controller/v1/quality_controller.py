from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.service.quality_rule_service import IQualityRuleService
from src.service.quality_rule_service import QualityRuleService
from src.repository.sqlite_quality_rule_repository import SQLiteQualityRuleRepository
from src.exceptions.quality_rule_exceptions import (
    QualityRuleNotFound,
    QualityRuleExists,
    QualityRuleIsDeactivated,
    QualityRuleIsActive
)
from src.schema.quality_rule_schema import QualityRuleSchema, QualityRuleUpdateSchema
from src.schema.responses_schema import QualityRuleObjectResponse


def get_quality_rule_service():
    
    return QualityRuleService(SQLiteQualityRuleRepository())


class QualityController:
    
    router = APIRouter()
    
    @router.post("/rule", status_code=201, response_model=QualityRuleObjectResponse)
    async def create_quality_rule(rule: QualityRuleSchema, quality_rule_service: IQualityRuleService = Depends(get_quality_rule_service)):
        try:
            response = quality_rule_service.create_rule(**rule.dict())
            return response
        
        except QualityRuleExists as e:
            
            return JSONResponse(
                status_code= status.HTTP_409_CONFLICT,
                content={"message": str(e)}
            )

    @router.get("/rule/{rule_id}")
    async def get_quality_rule(rule_id: int, quality_rule_service: IQualityRuleService = Depends(get_quality_rule_service)):
        try:
            response = quality_rule_service.read_rule_by_id(rule_id=rule_id)
            return response
        
        except QualityRuleNotFound as e:
            
            return JSONResponse(
                status_code= status.HTTP_404_NOT_FOUND,
                content={"message": str(e)}
            )
            
    @router.get("/rule/table/{target_table}")
    async def get_quality_rules_by_table(target_table: str, is_active: bool | None = True, quality_rule_service: IQualityRuleService = Depends(get_quality_rule_service)):
        
        return quality_rule_service.read_rules_by_target_table(target_table=target_table, is_active=is_active)

    @router.put("/rule/{rule_id}")
    async def update_quality_rule(rule_id: int, new_rule_data: QualityRuleUpdateSchema, quality_rule_service: IQualityRuleService = Depends(get_quality_rule_service)):
        try:
            response = quality_rule_service.update_rule(rule_id=rule_id, rule_data=new_rule_data.model_dump())
            return response
        
        except QualityRuleNotFound as e:
            
            return JSONResponse(
                status_code= status.HTTP_404_NOT_FOUND,
                content={"message": str(e)}
            )
        
        except QualityRuleIsDeactivated as e:
            
            return JSONResponse(
                status_code= status.HTTP_409_CONFLICT,
                content={"message": str(e)}
            )
            
        except QualityRuleExists as e:
            
            return JSONResponse(
                status_code= status.HTTP_409_CONFLICT,
                content={"message": str(e)}
            )