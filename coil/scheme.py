# -*- coding:utf-8 -*-

from .symbol import Symbol


class Scheme(object):

    """ """
    symbol_tables = {keyword: Symbol(keyword) for keyword in ['quote', 'if', 'set!', 'define', 'lambda', 'begin']}

    @classmethod
    def pause(cls, tokenizer):

        """ """
        return [cls.__symbolize(token, tokenizer) for token in tokenizer][0]

    @classmethod
    def evaluate(cls, token, environment):
        if isinstance(token, Symbol):
            return environment.find(token)[token]
        elif not isinstance(token, list):
            return token
        elif token[0] is cls.__symbol('quote'):
            (_, exp) = token
            return exp
        elif token[0] is cls.__symbol('if'):
            (_, test, conseq, alt) = token
            return Scheme.evaluate((conseq if Scheme.evaluate(test, environment) else alt), environment)
        elif token[0] is cls.__symbol('set!'):
            (_, var, exp) = token
            environment.find(var)[var] = Scheme.evaluate(exp, environment)
        elif token[0] is cls.__symbol('define'):
            (_, var, exp) = token
            environment[var] = Scheme.evaluate(exp, environment)
        elif token[0] is cls.__symbol('lambda'):
            (_, var, exp) = token
            return lambda *args: Scheme.evaluate(var, Environment(var, args, environment))
        elif token[0] is cls.__symbol('begin'):
            for exp in token[1:]:
                val = Scheme.evaluate(exp, env)
            return val
        else:
            exps = [Scheme.evaluate(exp, environment) for exp in token]
            proc = exps.pop(0)
            return proc(*exps)

    """ """
    @classmethod
    def __symbolize(cls, token, tokenizer):

        """ """
        if(token == '('):
            lists = []
            while True:
                next_token = next(tokenizer)
                if next_token == ')':
                    return lists
                else:
                    lists.append(cls.__symbolize(next_token, tokenizer))
        else:
            return cls.__atom(token)

    """ """
    @classmethod
    def __atom(cls, token):
        if token.isnumeric():
            return float(token)
        else:
            return cls.__symbol(token)

    """ """
    @classmethod
    def __symbol(cls, token):
        if token not in cls.symbol_tables:
            cls.symbol_tables[token] = Symbol(token)
        return cls.symbol_tables[token]