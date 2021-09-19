"""custom exceptions"""


class BaseXetraException(Exception):
    pass

class BucketNotFoundException(Exception):
    """
    exception that can be raised when s3 bucket not found
    """

    def __init__(self, endpoint_url):
        self.endpoint_url = endpoint_url

    def __repr__(self):
        return f"s3 bucket at {self.endpoint_url} not found"


class WrongFormatException(BaseXetraException):
    """
    Exception that can be raised when the format type
    given as parameter is not supported.
    """

    def __init__(self, format):
        self.format = format

    def __repr__(self):
        return f"file format {format} not supported"


class WrongMetaFileException(BaseXetraException):
    """
    Exception that can be raised when the meta file
    format is not correct.
    """
