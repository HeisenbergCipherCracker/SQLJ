class SQLJNG_Option_Error(Exception):
    def __init__(self, message='Invalid option.'):
        self.message = message
        super().__init__(self.message)

class SQLJNGBasicException(Exception):
    pass

class SQLJNGOptionError(SQLJNGBasicException):
    pass

class SQLJNGConnectionError(SQLJNGBasicException):
    pass
