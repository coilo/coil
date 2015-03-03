# -*- coding:utf-8 -*-

import io

from .tokenizer import Tokenizer
from .environment import Environment
from .scheme import Scheme


class Coil(object):
    def __init__(self, code):
        self.code = code
        self.reader = io.StringIO(code)

    def run(self):

        tokenizer = Tokenizer(self.reader).tokenizer()

        ##
        return Scheme.evaluate(Scheme.pause(tokenizer), Environment.namespace())
