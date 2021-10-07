from typing import Text
from .color import Color


class Report:
    def __init__(self, color: Color, verbose: bool) -> None:
        self._color: Color = color

        self._verbose = verbose

    def print_error(self, retval: Text) -> None:
        if type(retval) is Text:
            print(
                "{}[ERROR]{} {}".format(
                    self._color.error,
                    self._color.end,
                    retval
                )
            )

    def verbose(self, function: callable) -> None:
        if self._verbose:
            print(
                "{}[OK]{} {} passed".format(
                    self._color.success,
                    self._color.end,
                    function.__name__
                )
            )

    def handle_errors(self, retval: Text, function: callable) -> None:
        self.print_error(retval)

        self.verbose(function)
