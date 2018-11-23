class Nint(int):
    def __new__(cls, arg = 0):
        if isinstance(cls, str):
            total = 0
            for each in arg:
                total += ord(each)
            arg = total



