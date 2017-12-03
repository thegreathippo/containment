M_31 = 1, 3, 5, 7, 8, 10, 12
M_30 = 4, 6, 9, 11


class Session:

    def __init__(self):
        self._minutes = 0
        self._hours = 0
        self._day = 1
        self._month = 1
        self._year = 2015
        self.funds = 500

    def tick(self):
        self._advance_time()
        self._advance_date()

    @property
    def time(self):
        if self._hours < 10:
            hours = "0" + str(self._hours)
        else:
            hours = str(self._hours)
        if self._minutes < 10:
            minutes = "0" + str(self._minutes)
        else:
            minutes = str(self._minutes)
        return hours + ":" + minutes

    @property
    def date(self):
        if self._day < 10:
            day = "0" + str(self._day)
        else:
            day = str(self._day)
        if self._month < 10:
            month = "0" + str(self._month)
        else:
            month = str(self._month)
        return day + "/" + month + "/" + str(self._year)

    def _advance_time(self):
        self._minutes += 1
        if self._minutes == 60:
            self._minutes = 0
            self._hours += 1
            if self._hours == 24:
                self._hours = 0
                self._day += 1

    def _advance_date(self):
        if self._month in M_31:
            if self._day == 31:
                self._day = 1
                self._month += 1
        elif self._month in M_30:
            if self._day == 30:
                self._day = 1
                self._month += 1
        else:
            if self._day == 28:
                self._day = 1
                self._month += 1
        if self._month == 13:
            self._month = 1
            self._year += 1

