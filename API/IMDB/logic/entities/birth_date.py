class BirthDate:

    def __init__(self, day, month):
        self.day = day
        self.month = month

    @property
    def day(self):
        return self._day

    @day.setter
    def day(self, d):
        self._day = d

    @property
    def month(self):
        return self._month

    @month.setter
    def month(self, m):
        self._month = m

    def __str__(self):
        if 0 < self._day < 10:
            self._day = f"0{self._day}"
        if 0 < self._month < 10:
            self._month = f"0{self._month}"
        return f"month={self._month}&day={self._day}"
