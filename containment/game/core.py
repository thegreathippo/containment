from .session import Session
from kvy import App
from kvy import ScreenManager
from kvy import NumericProperty, StringProperty
from kvy import Clock


class GameApp(App):

    session = None
    date = StringProperty()
    time = StringProperty()
    stats = StringProperty()

    def build(self):
        window = MainWindow()
        return window

    def new_game(self):
        self.session = Session()
        Clock.schedule_interval(self.tick, 0.1)

    def add_funds(self):
        self.session.funds += 100

    def tick(self, *args):
        self.session.tick()
        self.time = self.session.time
        self.date = self.session.date
        self.update_stats()

    def update_stats(self):
        funds = "$" + str(self.session.funds) + "k"
        self.stats = " SITES:     {0}\n FUNDS:     {1}\n ".format(1, funds)


class MainWindow(ScreenManager):
    pass


