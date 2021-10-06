from typing import Text


class Color:
    def __init__(self) -> None:
        self.end: Text = "\033[0m"


    class __Color:
        def __init__(self, opacity: int) -> None:
            self.__opacity: int = opacity

            self.base: Text = "\033[{}{}m"

            self.black: Text = self.__formatColor(0)

            self.red: Text = self.__formatColor(1)

            self.green: Text = self.__formatColor(2)

            self.brown: Text = self.__formatColor(3)

            self.blue: Text = self.__formatColor(4)

            self.purple: Text = self.__formatColor(5)

            self.cyan: Text = self.__formatColor(6)

        def __formatColor(self, colorCode: int) -> Text:
            return self.base.format(self.__opacity, colorCode)


    @property
    def light(self) -> Text:
        return self.__Color(9)


    @property
    def dark(self) -> Text:
        return self.__Color(3)


    @property
    def error(self) -> Text:
        return self.light.red


    @property
    def warning(self) -> Text:
        return self.light.cyan


    @property
    def success(self) -> Text:
        return self.light.green