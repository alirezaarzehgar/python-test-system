from typing import Text
from .Color import Color


class Report:
    def __init__(self, color: Color, verbose: bool) -> None:
        self._color: Color = color

        self._verbose = verbose


    def printError(self, retval: Text) -> None:
        if type(retval) is Text:
            print(
                "{}[ERROR]{} {}".format(
                    self._color.error,
                    self._color.end,
                    retval
                )
            )

            exit(1)


    def verbose(self, function: callable) -> None:
        if self._verbose:
            print(
                "{}[OK]{} {} passed".format(
                    self._color.success,
                    self._color.end,
                    function.__name__
                )
            )


    def handleErrors(self, retval: Text, function: callable) -> None:
        self.printError(retval)

        self.verbose(function)
