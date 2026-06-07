class RepoError(Exception):
    """Base class for repository-related exceptions."""
    pass

class DeleteIsNotActive(RepoError):
    """Exception raised when attempting to delete a rule that is not active."""
    pass

class RevertDeleteIsActive(RepoError):
    """Exception raised when trying to revert delete on an active rule."""
    pass

class UpdateIsNotActive(RepoError):
    """Exception raised when trying to update an inactive rule."""
    pass