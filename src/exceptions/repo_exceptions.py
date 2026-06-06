class RepoError(Exception):
    """Base class for repository-related exceptions."""
    pass

class NotActive(RepoError):
    """Exception raised when a rule is not active."""
    pass

class RevertDeleteIsActive(RepoError):
    """Exception raised when trying to revert delete on an active rule."""
    pass

class UpdateIsNotActive(RepoError):
    """Exception raised when trying to update an inactive rule."""
    pass