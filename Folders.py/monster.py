import pygame
import random
import animation

class Monster(animation.animate_sprite):

    def __init__(self, game):
        super().__init__("mummy")
        self.game = game
        self.health = 100
        self.max_health = 100
        self.attack = 0.3
        self.rect = self.image.get_rect()
        self.rect.x = 1000 + random.randint(0, 300)
        self.rect.y = 540
        self.velocity = random.randint(1,3)
        self.start_animation()

    def damage(self, amount):
        self.health -= amount
        if self.health <= 0:
            self.rect.x = 1000 + random.randint(0, 300)
            self.velocity = random.randint(1,3)
            self.health = self.max_health

            if self.game.comet_event.is_full_loading():
                self.game.all_monster.remove(self)
                self.game.comet_event.attempt_fall()

    def update_animation(self):
        self.animate(loop=True)

    def update_health_bar(self, surface):
        bar_color = (111, 210, 46)
        back_bar_color = (60, 63, 60)
        bar_position = [self.rect.x + 10, self.rect.y - 20, self.health, 5]
        back_bar_position = [self.rect.x + 10, self.rect.y - 20, self.max_health, 5]

        pygame.draw.rect(surface, back_bar_color, back_bar_position)
        pygame.draw.rect(surface, bar_color, bar_position)


    def forward(self):
        if not self.game.check_collision(self, self.game.all_player):
            self.rect.x -= self.velocity
        else:
            self.game.player.damage(self.attack)

