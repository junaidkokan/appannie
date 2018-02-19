class AppAnnieException(Exception):
    def __init__(self, message, *args):
        super(AppAnnieException, self).__init__(message, *args)

class AppAnnieBadRequestException(AppAnnieException):
    ERROR_CODE = 400
    def __init__(self, *args):
        self.message = "A common root cause is a misuse of the parameter, check the syntax and the range available for each parameter"
        super(AppAnnieBadRequestException, self).__init__(self.message, *args)


class AppAnnieUnauthorizedException(AppAnnieException):
    ERROR_CODE = 401
    def __init__(self, message, *args):
        self.message = "Please ensure your API key is valid"
        super(AppAnnieUnauthorizedException, self).__init__(message, *args)
        
        
class AppAnnieNoPermissionException(AppAnnieException):
    ERROR_CODE = 403
    def __init__(self, *args):
        self.message = "No permission. This error will usually happen if you try to access to a resource that is not part of your subscription"
        super(AppAnnieNoPermissionException, self).__init__(self.message, *args)
    
    
class AppAnnieNotFoundException(AppAnnieException):
    ERROR_CODE = 404
    def __init__(self, *args):
        self.message = "Not found. Check if the URL of the API is correct"
        super(AppAnnieNotFoundException, self).__init__(self.message, *args)
        

class AppAnnieMethodNotSuppprtedException(AppAnnieException):
    ERROR_CODE = 405
    def __init__(self, message, *args):
        self.message = "HTTP method is not supported"
        super(AppAnnieMethodNotSuppprtedException, self).__init__(message, *args)


class AppAnnieTemporaryBlacklistingException(AppAnnieException):
    ERROR_CODE = 428
    def __init__(self, message, *args):
        self.message = "Temporary blacklisting"
        super(AppAnnieTemporaryBlacklistingException, self).__init__(message, *args)
        

class AppAnnieRateLimitExceededException(AppAnnieException):
    ERROR_CODE = 429
    def __init__(self, *args):
        self.message = "Rate limit exceeded"
        super(AppAnnieRateLimitExceededException, self).__init__(self.message, *args)

        
class AppAnnieInternalErrorException(AppAnnieException):
    ERROR_CODE = 500
    def __init__(self, *args):
        self.message = "Internal error"
        super(AppAnnieInternalErrorException, self).__init__(self.message, *args)


class AppAnnieServiceUnavailableException(AppAnnieException):
    ERROR_CODE = 503
    def __init__(self, *args):
        self.message = "Service unavailable due to maintenance"
        super(AppAnnieServiceUnavailableException, self).__init__(self.message, *args)
