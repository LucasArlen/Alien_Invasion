class Settings:
    def __init__(self):
        # Configurações de Tela
        self.screen_width = 1100
        self.screen_height = 700
        self.bg_color = (66, 81, 170)
        self.ship_speed_factor = 1.5

        # Configurações do Projétil
        self.bullet_speed_factor = 3
        self.bullet_width = 3
        self.bullet_height = 15
        self.bullet_color = 60, 60, 60
        self.bullets_allowed = 3

        # Configurações dos alienígenas
        self.alien_speed_factor = 0.2
        self.fleet_drop_speed = 5

        # fleet_direction igual a 1 representa direita; -1 representa a esquerda
        self.fleet_direction = 1