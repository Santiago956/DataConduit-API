
class QualityRuleError(Exception):
    """Base exception for all quality rule related errors."""
    pass

class QualityRuleIsDeactivated(QualityRuleError):
    """Exception raised when trying to update a deactivated quality rule."""
    pass

class QualityRuleIsActive(QualityRuleError):
    """Exception raised when trying to activate an already active quality rule."""
    pass

class QualityRuleNotFound(QualityRuleError):
    """Exception raised when a quality rule is not found."""
    pass

class QualityRuleExists(QualityRuleError):
    """Exception raised when a quality rule already exists."""
    pass