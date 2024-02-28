import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent
from comet import Comet

class Game:

    def __init__(self):
        self.is_playing = False
        self.game_over_statut = False
        self.is_replaying = False
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        self.monster = Monster(self)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        self.comet_event = CometFallEvent(self)

    def restart(self):
        self.is_replaying = True

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.rect.x = 300
        self.comet_event.all_comet = pygame.sprite.Group()
        self.game_over_statut = True
        self.is_playing = False
        self.is_playing = self.is_replaying


    def update(self, screen):
        screen.blit(self.player.image, self.player.rect)
        self.all_monster.draw(screen)

        self.comet_event.all_comet.draw(screen)

        self.player.all_projectile.draw(screen)
        self.player.update_health_bar(screen)

        self.player.animate()

        self.comet_event.update_bar(screen)

        for comet in self.comet_event.all_comet:
            comet.fall()

        for projectile in self.player.all_projectile:
            projectile.move()

        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_rigth()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()

    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)

    def spawn_monster(self):
        monster1 = Monster(self)
        self.all_monster.add(monster1)

