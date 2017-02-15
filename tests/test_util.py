#!/usr/bin/env python

"""Unit tests for M2Crypto.Rand.

Copyright (C) 2006 Open Source Applications Foundation (OSAF).
All Rights Reserved.
"""

import os
import warnings
try:
    import unittest2 as unittest
except ImportError:
    import unittest

from M2Crypto import util

# if six.PY2:
#     def py3bytes(x):
#         # type: (bytes) -> bytes
#         return x
# 
#     def py3str(x):
#         # type: (str) -> str
#         return x
# else:
#     def py3bytes(x):
#         # type: (AnyStr) -> bytes
#         return x if isinstance(x, bytes) else x is not None and bytes(x, encoding="utf8") or x
# 
#     def py3str(x):
#         # type: (AnyStr) -> str
#         return x if isinstance(x, str) else x is not None and x.decode("utf8") or x


class UtilTestCase(unittest.TestCase):
    def test_py3bytes(self):
        self.assertIsInstance(util.py3bytes('test'), bytes)

    def test_py3str(self):
        self.assertIsInstance(util.py3str('test'), str)

    def test_py3bytes_str(self):
        self.assertIsInstance(util.py3bytes(u'test'), bytes)

    def test_py3str_str(self):
        self.assertIsInstance(util.py3str(u'test'), str)

    def test_py3bytes_bytes(self):
        self.assertIsInstance(util.py3bytes(b'test'), bytes)

    def test_py3str_bytes(self):
        self.assertIsInstance(util.py3str(b'test'), str)

    def test_py3bytes_None(self):
        self.assertIsInstance(util.py3bytes(None), NoneType)

    def test_py3str_None(self):
        self.assertIsInstance(util.py3str(None), NoneType)


def suite():
    suite = unittest.TestSuite()
    suite.addTest(unittest.makeSuite(UtilTestCase))
    return suite


if __name__ == '__main__':
    unittest.TextTestRunner().run(suite())
