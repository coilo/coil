# -*- coding:utf-8 -*-


# All coil exceptions should also be derived from this class.
class CoilError(Exception):
    pass


# Raised when the parser encounters a syntax error.
class CoilSyntaxError(CoilError):
    pass


# Raised when an error is detected
# that doesn’t fall in any of the other categories.
class CoilRuntimeError(CoilError):
    pass
