from fastapi import HTTPException, status
from functools import wraps


def handle_exceptions(func):
    @wraps(func)  # Preserves the metadata of the original function
    async def wrapper(*args, **kwargs):
        try:
            result = await func(*args, **kwargs)  # Support for async functions
            return result
        except HTTPException as e:
            # Re-raise known HTTPExceptions without modification
            raise e
        except ValueError as e:
            raise HTTPException(
                status_code=status.HTTP_400_BAD_REQUEST,
                detail=f"Invalid input: {str(e)}"
            )
        except Exception as e:
            raise HTTPException(
                status_code=status.HTTP_500_INTERNAL_SERVER_ERROR,
                detail="An unexpected error occurred"
            )

    return wrapper
