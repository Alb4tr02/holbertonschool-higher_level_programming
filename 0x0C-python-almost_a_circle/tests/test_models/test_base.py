#!/usr/bin/env python
"""Test for class base"""


import unittest
from models.base import Base


class TestBaseClass(unittest.TestCase):
    """TestBase Class"""

    def test_base(self):
        """Cases"""
        a1 = Base(-32)
        a2 = Base(-2)
        a3 = Base(0)
        a4 = Base(-0)
        a5 = Base(32)
        a6 = Base(3200)
        a7 = Base(1)
        a8 = Base()
        self.assertEqual(a1.id, -32)
        self.assertEqual(a2.id, -2)
        self.assertEqual(a3.id, 0)
        self.assertEqual(a4.id, 0)
        self.assertEqual(a5.id, 32)
        self.assertEqual(a6.id, 3200)
        self.assertEqual(a7.id, 1)
        self.assertEqual(a8.id, 1)
        Base.id = 34
        a9 = Base()
        self.assertEqual(a9.id, 2)
    def test_medicuenta(self):
        """Cases"""
        a1 = Base(-32)
        a2 = Base(-2)
        a3 = Base(0)
        a4 = Base(-0)
        a5 = Base(32)
        a6 = Base(3200)
        a7 = Base(1)
        self.assertEqual(a1.id, -32)
        self.assertEqual(a2.id, -2)
        self.assertEqual(a3.id, 0)
        self.assertEqual(a4.id, 0)
        self.assertEqual(a5.id, 32)
        self.assertEqual(a6.id, 3200)
        self.assertEqual(a7.id, 1)
