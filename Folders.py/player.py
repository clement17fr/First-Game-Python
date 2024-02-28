import pygame
from projectile import Projectile
import animation

class Player(animation.animate_sprite):

    def __init__(self, game):

        super().__init__("player")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 10
        self.velocity = 12
        self.all_projectile = pygame.sprite.Group()
        self.rect = self.image.get_rect()
        self.rect.x = 400
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount

        else:
            self.game.game_over()

    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 45, self.rect.y + 10, self.health, 5]
        back_bar_position = [self.rect.x + 45, self.rect.y + 10, self.max_health, 5]
        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def launch_projectile(self):
        self.all_projectile.add(Projectile(self))
        self.start_animation()

    def move_rigth(self):
        if not self.game.check_collision(self, self.game.all_monster):
            self.rect.x += self.velocity

    def move_left(self):
        self.rect.x -= self.velocity