# -*- coding: utf-8 -*-
import io
import sys
import unittest
import coil


class CoilTest(unittest.TestCase):

    def testNumeric(self):
        with open('scheme/numeric.scm') as f:
            for code in f.readlines():

                """ """
                coil.Coil(code).run()
    def testBoolean(self):
        with open('scheme/boolean.scm') as f:
            for code in f.readlines():

                """ """
                coil.Coil(code).run()

def suite():
    suite = unittest.TestSuite()
    suite.addTests(unittest.makeSuite(CoilTest))
    return suite

if __name__ == "__main__":
    unittest.main()
