#!/usr/bin/env python
"""Test for class base"""


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """TestBase Class"""

    def test_base(self):
        """Cases"""
        self.a1 = Base(-32)
        self.a2 = Base(-2)
        self.a3 = Base(0)
        self.a4 = Base(-0)
        self.a5 = Base(32)
        self.a6 = Base(3200)
        self.a7 = Base(1)
        self.a8 = Base()
        self.assertEqual(self.a1.id, -32)
        self.assertEqual(self.a2.id, -2)
        self.assertEqual(self.a3.id, 0)
        self.assertEqual(self.a4.id, 0)
        self.assertEqual(self.a5.id, 32)
        self.assertEqual(self.a6.id, 3200)
        self.assertEqual(self.a7.id, 1)
        self.assertEqual(self.a8.id, 1)
        Base.id = 34
        self.a9 = Base()
        self.assertEqual(self.a9.id, 2)

if __name__ == "__main__":
    unittest.main()
