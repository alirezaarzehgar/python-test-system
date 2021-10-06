from typing import List

from TestSystem.Output.Color import Color
from . import Report, Runable


class TestSystem():
    def __init__(self) -> None:
        color = Color()
        self.report = Report(color, True)

    def iterate(self, classes: List[Runable]):
        for className in classes:
            if hasattr(className, "run"):
                className.run()
            else:
                self.report.printError("has no attribute 'run'")