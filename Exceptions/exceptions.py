from warnings import warn

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

class SQLJNGUserExit(SQLJNGBasicException):
    pass

class SQLJNGNotOptionSelected(SQLJNGBasicException):
    pass

class SQLJNGInstallationError(SQLJNGBasicException):
    pass

class SQLJNGUserExit(SystemExit):
    pass

class SQLJNGApiError(SQLJNGBasicException):
    pass

class SQLJNGProxyFiltringError(SQLJNGBasicException):
    pass

class SQLJNGTimeExpiredError(SQLJNGBasicException):
    pass

class SQLJNGUnknowProxyError(SQLJNGBasicException):
    pass

class SQLJNGOSError(SQLJNGBasicException):
    pass

class SQLJNGFatalError(SQLJNGBasicException):
    pass

class SQLJNGModuleError(SQLJNGBasicException):
    pass

class SQLJNGInputModuleError(SQLJNGBasicException):
    pass

class SQLJNGDependenciesError(SQLJNGBasicException):
    pass

class SQLJNGUserAborted(SQLJNGBasicException):
    pass




