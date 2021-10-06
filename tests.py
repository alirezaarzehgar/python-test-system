import unittest
from unittest.main import main
from TestSystem.TestSystem import TestSystem

from TestSystem.Runable import Runable


class A(Runable):
    def run():
        print("hello")


class TestOfTestSystem(unittest.TestCase):
    def testIterate(self):
        TestSystem().iterate([
            A
        ])

        assert True == True

if __name__ == '__main__':
    unittest.main()
    