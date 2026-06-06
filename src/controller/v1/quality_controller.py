from fastapi import APIRouter, Depends, status
from fastapi.responses import JSONResponse

from src.service.quality_rule_service import IQualityRuleService
from src.service.quality_rule_service import QualityRuleService
from src.repository.sqlite_quality_rule_repository import SQLiteQualityRuleRepository
from src.exceptions.quality_rule_exceptions import QualityRuleNotFound


def get_quality_rule_service():
    
    return QualityRuleService(SQLiteQualityRuleRepository())


class QualityController:
    
    router = APIRouter()
    
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