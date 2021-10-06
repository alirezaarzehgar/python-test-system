# python-test-system
a small module for iterating classes and automate testing suitable for system/behavior testing.

## usage

You should import TestSystem on your project :

```python
from TestSystem.TestSystem import TestSystem
```

Then you should create a class and implement from Runable interface.

```python
from TestSystem.Runable import Runable


class A(Runable):
    def run():
        print("hello!")
        return True
```

After creating class you just should run interate method from `TestSystem` class.

```python
TestSystem().iterate([
            classA,
            classB,
            classC
        ])
```