from typing import List

from TestSystem.Output.Color import Color
from . import Report, Runable


class TestSystem():
    def __init__(self) -> None:
        color = Color()
        self.report = Report(color, True)

    def iterate(self, classes: List[Runable]) -> List[bool]:
        result = []

        for className in classes:
            if className != None and hasattr(className, "run"):
                ret = None

                try:
                    ret = className.run()
                except:
                    ret = False

                if ret == None:
                    ret = False

                result.append(ret)

            else:
                self.report.printError("has no attribute 'run'")

                result.append(False)

        return result