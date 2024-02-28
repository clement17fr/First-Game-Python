import pygame
from player import Player
from monster import Monster
from comet_event import CometFallEvent
from comet import Comet

class Game:

    def __init__(self):
        #definir si notre jeu a commencé ou non
        self.is_playing = False
        self.game_over_statut = False
        self.is_replaying = False
        #generer notre joueur
        self.all_player = pygame.sprite.Group()
        self.player = Player(self)
        self.all_player.add(self.player)
        #groupe de monstre
        self.monster = Monster(self)
        self.all_monster = pygame.sprite.Group()
        self.pressed = {}
        #genere l'evenement de pluie de comete
        self.comet_event = CometFallEvent(self)

    def restart(self):
        self.is_replaying = True

    def start(self):
        self.is_playing = True
        self.spawn_monster()
        self.spawn_monster()

    def game_over(self):
        #remetre le jeu a neuf
        self.all_monster = pygame.sprite.Group()
        self.player.health = self.player.max_health
        self.player.rect.x = 300
        self.comet_event.all_comet = pygame.sprite.Group()
        self.game_over_statut = True
        self.is_playing = False
        self.is_playing = self.is_replaying


    def update(self, screen):
        # appliquer l'image de mon joueur
        screen.blit(self.player.image, self.player.rect)

        # appliquer l'ensemble des image de mon groupe de monstre
        self.all_monster.draw(screen)

        #appliquer l'ensemble des image de mon groupe de comete
        self.comet_event.all_comet.draw(screen)

        # appliquer l'enselble des image de mes projectiles
        self.player.all_projectile.draw(screen)
        self.player.update_health_bar(screen)

        #appliquer l'animation du joueur
        self.player.animate()

        #actualiser la bar d'evenement du jeu
        self.comet_event.update_bar(screen)

        #recupere les comet
        for comet in self.comet_event.all_comet:
            comet.fall()

        # recuperer les projectile du joueur
        for projectile in self.player.all_projectile:
            projectile.move()

            # recuperer les monstre de notre jeu
        for monster in self.all_monster:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()


        # verifier si le joueur souhaite aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < screen.get_width():
            self.player.move_rigth()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.move_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self):
        monster1 = Monster(self)
        self.all_monster.add(monster1)

