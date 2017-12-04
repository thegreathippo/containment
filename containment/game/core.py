from .session import Session
from kvy import App
from kvy import ScreenManager
from kvy import NumericProperty, StringProperty
from kvy import Clock


class GameApp(App):

    _speed = 1
    session = None
    date = StringProperty()
    time = StringProperty()
    fs = StringProperty()  # foundation status
    ws = StringProperty()  # world status
    title = "Containment: Apocalypse"

    def build(self):
        window = MainWindow()
        return window

    def new_game(self):
        self.session = Session()
        Clock.schedule_interval(self.tick, 0.05)

    def tick(self, *args):
        if self._speed:
            self.session.tick()
            self.time = self.session.time
            self.date = self.session.date
        self.update_status()

    def update_status(self):
        self.fs = _foundation_status(self.session.foundation)
        self.ws = _world_status(self.session.world)

    def pause(self):
        self._speed = 0

    def resume(self):
        self._speed = 1


class MainWindow(ScreenManager):
    pass


def _foundation_status(foundation):
    agent = " PERSONNEL:  {0}".format(foundation.personnel)
    sites = " SITES:      {0}".format(foundation.sites)
    funds = " FUNDS:      ${0}k".format(foundation.funds)
    anoma = " ANOMALIES:  {0}/{1}".format(foundation.anomalies, foundation.max_anomalies)
    resea = " RESEARCH:   {0}".format(foundation.research)
    data = agent + "\n" + sites + "\n" + anoma + "\n" + funds + "\n" + resea
    return data


def _world_status(world):
    popul = " POPULATION: {0}".format(world.population)
    anoma = " ANOMALIES:  {0}".format(world.anomalies)
    panic = " PANIC:      {0}".format(world.panic)
    data = popul + "\n" + anoma + "\n" + panic
    return data
