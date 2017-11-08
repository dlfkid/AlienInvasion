class GameState():
    #跟踪游戏的统计信息
    def __init__(self,settings):
        self.settings = settings
        self.reset_state()

    def reset_state(self):
        self.ships_left = self.settings.ship_limit