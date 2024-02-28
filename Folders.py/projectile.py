import pygame
from pygame import Surface, SurfaceType

class Projectile(pygame.sprite.Sprite):

    def __init__(self, player):
        super().__init__()
        self.player = player
        self.velocity = 10
        self.image = pygame.image.load("assets/projectile.png")
        self.rect = self.image.get_rect()
        self.image = pygame.transform.scale(self.image, (50, 50))
        self.rect.x = player.rect.x + 120
        self.rect.y = player.rect.y + 90
        self.origin_image = self.image
        self.angle = 0

    def rotate(self):
        self.angle += 12
        self.image = pygame.transform.rotozoom(self.origin_image, self.angle, 1)

    def remove(self):
        self.player.all_projectile.remove(self)

    def move(self):
        self.rect.x += self.velocity
        self.rotate()

        for monster in self.player.game.check_collision(self, self.player.game.all_monster):
            self.remove()
            monster.damage(self.player.attack)

        if self.rect.x > 1080:
            self.remove()
            print("le projectile a ete suprimer")


