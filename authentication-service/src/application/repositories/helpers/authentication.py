from functools import wraps

from src.application.repositories.authentication import AuthenticationRepository


def verify_if_user_exists(func):

    @wraps(func)
    async def wrapper(*args, **kwargs):
        repository_arg = [arg for arg in args if isinstance(arg, AuthenticationRepository)]
        if not repository_arg:
            return None
        repository = repository_arg[0]
        user_id = kwargs['user_id']
        if not user_id or not await repository.get(user_id=user_id):
            return None
        return await func(*args, **kwargs)

    return wrapper
