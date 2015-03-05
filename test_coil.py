# -*- coding: utf-8 -*-
import io
import sys
import unittest
import coil


class CoilTest(unittest.TestCase):

    def testNumeric(self):

        """ Coil#run testcase. """
        with open('scheme/numeric.scm') as f:
            for code in f.readlines():
                coil.Coil(code).run()

    def testBoolean(self):

        """  Coil#run testcase. """
        with open('scheme/boolean.scm') as f:
            for code in f.readlines():

                """ """
                coil.Coil(code).run()

    def testConditionals(self):

        """ Coil#run testcase. """
        with open('scheme/conditionals.scm') as f:
            for code in f.readlines():

                """ """
                coil.Coil(code).run()

    def testSyntaxError(self):

        """  Coil#run testcase. """
        code = "(+ 1 2))"
        with self.assertRaises(coil.exception.CoilSyntaxError):
            coil.Coil(code).run()

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(CoilTest))
    return suite

if __name__ == "__main__":
    unittest.main()
