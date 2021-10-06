from typing import List

from TestSystem.Output.Color import Color
from . import Report, Runable


class TestSystem():
    def __init__(self) -> None:
        self.report = Report(Color, True)
        pass

    def iterate(self, classes: List[Runable]):
        for className in classes:
            if className != None:
                className.run()
            else:
                pass