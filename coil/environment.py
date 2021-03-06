# -*- coding: utf-8 -*-

import math
import operator


class Environment(dict):

    def __init__(self, params=(), args=(), outer=None):

        """ """
        self.update(zip(params, args))
        self.outer = outer

    def find(self, variable):

        """ """
        return self if variable in self else self.outer.find(variable)

    @classmethod
    def namespace(cls):

        """ """
        def assertion(variable):
            assert variable

        """ """
        def assertion_equals(expected, actual):
            assert (expected == actual)

        environment = Environment()

        """ """
        environment.update({
            '+': operator.add,
            '-': operator.sub,
            '*': operator.mul,
            '/': operator.floordiv,
            '>': operator.gt,
            '<': operator.lt,
            '>=': operator.ge,
            '<=': operator.le,
            '=': operator.eq,
            'not': operator.not_,
            'cons': lambda x, y: [x] + y,
            'car': lambda x: x[0],
            'cdr': lambda x: x[1:],
            'boolean?': lambda x: isinstance(x, bool),
            'assert': lambda x: assertion(x),
            'assert-equal': lambda x, y: assertion_equals(x, y)
        })
        return environment
