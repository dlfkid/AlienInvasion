class Settings():
    #储存游戏设置的类
    def __init__(self):
        #初始化游戏的设置
        #屏幕设置
        self.screen_width = 1200
        self.screen_height = 600
        self.bg_color = (230,230,230)
        #飞船速度设置
        self.ship_speed_factor = 5
        #飞船上限
        self.ship_limit = 4
        #子弹设置
        self.bullet_speed_factor = 20
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60,60,60
        self.bullet_maximun = 5
        #外星人速度设置
        self.enemy_speed = 2
        self.fleet_drop_speed = 20
        #外星人飞行方向，1表示右移，-1表示作移
        self.fleet_direction = 1
