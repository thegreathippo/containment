M_31 = 1, 3, 5, 7, 8, 10, 12
M_30 = 4, 6, 9, 11

#  FOUNDATION
SITES = 1
FUNDS = 10
PERSONNEL = 0
FOUNDATION_ANOMALIES = 0
RESEARCH = 0

#  WORLD
PANIC = 0
WORLD_ANOMALIES = 1000
POPULATION = 7121416419

#  FORMULAS
TICK = 1
SITE_SPACE = 25
ANOMALY_PANIC = 0.002
POP_GROWTH = 0.0000000037
ANOMALY_RESEARCH = 0.005


class Session:

    def __init__(self):
        self._minutes = 0
        self._hours = 0
        self._day = 1
        self._month = 1
        self._year = 2015
        self.world = World()
        self.foundation = Foundation()

    def acquire_anomaly(self):
        self.foundation.anomalies += 1
        self.world.anomalies -= 1

    def tick(self):
        self._advance_time()
        self._advance_date()
        self._advance_game()

    def _advance_game(self):
        self.world.population += int(self.world.population * POP_GROWTH)
        self.world.panic += int(self.world.anomalies * ANOMALY_PANIC)
        self.foundation.research += int(self.foundation.researchers + (self.foundation.anomalies * ANOMALY_RESEARCH))

    def _advance_time(self):
        self._minutes += TICK
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


class World:
    def __init__(self):
        self.population = POPULATION
        self.panic = PANIC
        self.anomalies = WORLD_ANOMALIES


class Foundation:
    def __init__(self):
        self.funds = FUNDS
        self.personnel = PERSONNEL
        self.sites = SITES
        self.anomalies = FOUNDATION_ANOMALIES
        self.research = RESEARCH
        self.agents = 0
        self.researchers = 0

    @property
    def max_anomalies(self):
        return self.sites * SITE_SPACE
