from typing import List

from . import Report, Runable, Color


class TestSystem():
    def __init__(self) -> None:
        color = Color()
        self.report = Report(color, True)

    def iterate(self, classes: List[Runable]) -> List[bool]:
        result = []

        for class_name in classes:
            if class_name != None and hasattr(class_name, "run"):
                ret = None

                try:
                    ret = class_name.run()
                except:
                    ret = False

                if ret == None:
                    ret = False

                result.append(ret)

            else:
                self.report.print_error("has no attribute 'run'")

                result.append(False)

        return result
