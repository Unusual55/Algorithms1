class Activity:
    def __init__(self, start: int, end: int):
        self.s = start
        self.e = end

    def is_overlapped(self, other):
        return self.e <= other.s or self.s >= other.e
