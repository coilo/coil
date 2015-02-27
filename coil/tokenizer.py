# -*- coding:utf-8 -*-

import re
import io


class Tokenizer(object):

    def __init__(self, code):
        self.code = code

    def tokenizer(self):

        """ """
        tokenizer = r'''\s*(,@|[('`,)]|"(?:[\\].|[^\\"])*"|;.*|[^\s('"`,;)]*)(.*)'''
        line = ''

        """ """
        while True:
            if line == '':
                line = self.code.readline()
            if line == '':
                raise StopIteration

            token, line = re.match(tokenizer, line).groups()
            if token != '' and not token.startswith(';'):
                yield token
