import pygame
from comet import Comet

class CometFallEvent(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.comet = Comet(self)
        self.percent = 1
        self.percent_speed = 30
        self.all_comet = pygame.sprite.Group()
        self.fall_mode = False

    def add_percent(self):
        self.percent += self.percent_speed/60

    def is_full_loading(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):

        for i in range (1, 10):
            self.all_comet.add(Comet(self))

    def attempt_fall(self):
        if self.is_full_loading() and len(self.game.all_monster) == 0:
            print("pluie de comete")
            self.meteor_fall()
            self.fall_mode = True



    def update_bar(self, surface):
        self.add_percent()
        pygame.draw.rect(surface, (0,0,0), [
            0,
            surface.get_height() - 10,
            surface.get_width(),
            10
        ])
        pygame.draw.rect(surface, (187, 11, 11), [
            0,
            (surface.get_height() - 10),
             (surface.get_width()/100)*self.percent,
            10
        ])


