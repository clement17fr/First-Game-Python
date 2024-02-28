import pygame
from monster import Mummy, Alien
import random


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        self.comet_event = comet_event
        self.damage = 10
        self.velocity = random.randint(2,6)
        self.image = pygame.image.load("assets/comet.png")
        self.rect = self.image.get_rect()
        self.rect.x = random.randint(0, 1080)
        self.rect.y = -random.randint(0, 800)

    def remove(self):
        self.comet_event.all_comet.remove(self)

        if len(self.comet_event.all_comet) == 0:
            print("l'evenement est finie")
            # remettre la bar a zero
            self.comet_event.reset_percent()
            self.comet_event.game.start()

    def fall(self):
        self.rect.y += self.velocity

        if self.rect.y >= 500:
            self.remove()
            if len(self.comet_event.all_comet) == 0:
                print("la pluie de comete est fini")
                self.comet_event.reset_percent()
                self.comet_event.fall_mode = False

        if self.comet_event.game.check_collision(
            self, self.comet_event.game.all_player
        ):
            print("joueur toucher")
            self.remove()
            self.comet_event.game.player.damage(20)
