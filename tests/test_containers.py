"""Tests for the container functions"""


import unittest
from batteries.containers import Array


class TestArray(unittest.TestCase):
    def test_filter(self):
        data = [{"key": 1}, {"key": 2}, {"key": 2}]
        array = Array(data)
        array = array.filter(lambda x: x["key"] == 2)
        self.assertEqual(2, array.length())
        self.assertTrue(all([x["key"] == 2 for x in array.all()]))
