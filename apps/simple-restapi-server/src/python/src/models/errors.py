# Repository Errors 

class RepositoryErrorCodes:
    DATABASE_CONNECTION_CREATE_FAILED = 1001
    DATABASE_CONNECTION_CLOSE_FAILED = 1002
    DATABASE_READ_FAILED = 1003
    DATABASE_WRITE_FAILED = 1004
    USER_NOT_FOUND = 1005
    USER_ALREADY_EXISTS = 1006
    USER_INVALID_DATA = 1007
    USER_INVALID_RECORD = 1008
    GENERIC_REPOSITORY_ERROR = 1009

    @staticmethod
    def get_error_message(error_code: int):
        error_messages = {
            RepositoryErrorCodes.DATABASE_CONNECTION_CREATE_FAILED: "database connection failed",
            RepositoryErrorCodes.DATABASE_CONNECTION_CLOSE_FAILED: "database connection close failed",
            RepositoryErrorCodes.DATABASE_READ_FAILED: "database read failed",
            RepositoryErrorCodes.DATABASE_WRITE_FAILED: "database write failed",
            RepositoryErrorCodes.USER_NOT_FOUND: "user not found",
            RepositoryErrorCodes.USER_ALREADY_EXISTS: "user already exists",
            RepositoryErrorCodes.USER_INVALID_DATA: "invalid user data",
            RepositoryErrorCodes.USER_INVALID_RECORD: "invalid user record in the database, could not be parsed",
            RepositoryErrorCodes.GENERIC_REPOSITORY_ERROR: "generic repository error"
        }
        return error_messages.get(error_code, "unknown error")


class RepositoryError(Exception):
    
    def __init__(self, error_code: int):
        self.message = RepositoryErrorCodes.get_error_message(error_code)
        self.error_code = error_code
        super().__init__(self.message)

    def __str__(self) -> str:
        return f"repository error: {self.error_code}: {self.message}"
    

class DatabaseError(RepositoryError):
    pass


class UserError(RepositoryError):
    pass


# Service Errors

class ServiceErrorCodes:
    INTERNAL_SERVER_ERROR = 2001
    BAD_REQUEST = 2002
    NOT_FOUND = 2003

    @staticmethod
    def get_error_message(error_code: int):
        error_messages = {
            ServiceErrorCodes.INTERNAL_SERVER_ERROR: "internal server error",
            ServiceErrorCodes.BAD_REQUEST: "bad request",
            ServiceErrorCodes.NOT_FOUND: "not found"
        }
        return error_messages.get(error_code, "unknown error")
    

class ServiceError(Exception): 
    def __init__(self, error_code: int):
        self.message = ServiceErrorCodes.get_error_message(error_code)
        self.error_code = error_code
        super().__init__(self.message)

    def __str__(self) -> str:
        return super().__str__()


class InternalServerError(ServiceError):
    pass


class BadRequestError(ServiceError):
    pass


class NotFoundError(ServiceError):
    pass
