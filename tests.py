import unittest
from test_system import TestSystem, Runable


class A(Runable):
    def run():
        print("hello!")
        return True


class B():
    pass


class C(Runable):
    pass


class D(Runable):
    def run():
        print("without return")


class TestOfTestSystem(unittest.TestCase):
    def test_iterate_fail(self):
        results = TestSystem().iterate([
            None,
            B,
            C,
            D,
        ])

        for result in results:
            assert not result

    def test_iterate_pass(args):
        results = TestSystem().iterate([
            A
        ])

        for result in results:
            assert result == True


if __name__ == '__main__':
    unittest.main()
