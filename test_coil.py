# -*- coding: utf-8 -*-
import io
import sys
import unittest
import coil


class CoilTest(unittest.TestCase):

    def testNumeric(self):
        with open('scheme/numeric.scm') as f:
            code = f.read()

        self.assertEqual(15.0, coil.Coil(code).run())

if __name__ == "__main__":
    unittest.main()
