import typing


class Square:
    EMPTY = " "

    def __init__(self, value: str):
        self.valid_values = []
        self.value = None

        if value == self.EMPTY:
            self.set_value(None)
        else:
            self.set_value(int(value))

    def is_set(self) -> bool:
        return self.value is not None

    def get_value(self) -> typing.Optional[int]:
        return self.value

    def set_value(self, new_value: typing.Optional[int]):
        self.value = new_value

    def add_valid_value(self, value: int):
        self.valid_values.append(value)