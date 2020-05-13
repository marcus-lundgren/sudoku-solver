class Square:
    EMPTY = " "

    def __init__(self, value: str):
        if value == self.EMPTY:
            self.set_value(None)
        else:
            self.set_value(int(value))

    def is_set(self):
        return self.value != None

    def get_value(self):
        return self.value

    def set_value(self, new_value: int):
            self.value = new_value