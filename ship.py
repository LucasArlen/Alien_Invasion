import pygame


class Ship:

    def __init__(self, ai_settings, screen):
        self.screen = screen
        self.ai_settings = ai_settings

        # Carrega a imagem da espaçonave e obtém seu rect(retângulo)
        self.image = pygame.image.load('images/spaceship.bmp')
        self.rect = self.image.get_rect()
        self.screen_rect = screen.get_rect()

        # Inicializa a espaçonave na parte inferior central da tela
        self.rect.centerx = self.screen_rect.centerx
        self.rect.bottom = self.screen_rect.bottom

        # Armazena um valor decimal para o centro da nave
        self.center = float(self.rect.centerx)

        # Inicializando o flag de movimento
        self.moving_right = False
        self.moving_left = False

    def update(self):
        # Atualiza o valor do centro da nave e não do retângulo
        # E não permite que a nave ultrapasse as bordas
        if self.moving_right and self.rect.right < self.screen_rect.right:
            self.center += self.ai_settings.ship_speed_factor
        if self.moving_left and self.rect.left > 0:
            self.center -= self.ai_settings.ship_speed_factor

        self.rect.centerx = self.center


    def center_ship(self):
        """Centraliza a espaçonave na tela."""
        self.center = self.screen_rect.centerx

    def blitme(self):
        self.screen.blit(self.image, self.rect)

