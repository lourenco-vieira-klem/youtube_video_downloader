class CustomError(Exception):
    def __init__(self, message="") -> None:
        self.message = message

class NotFoundError(CustomError):
    ...

class ConfigError(CustomError):
    ...
