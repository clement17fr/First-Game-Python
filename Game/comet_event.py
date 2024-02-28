import pygame
from comet import Comet

class CometFallEvent(pygame.sprite.Sprite):

    def __init__(self, game):
        super().__init__()
        self.game = game
        self.comet = Comet(self)
        self.percent = 1
        self.percent_speed = 30
        #creer un groupe de comete
        self.all_comet = pygame.sprite.Group()
        self.fall_mode = False


    #definir une methode pour ajouter un pourcentage a notre bar
    def add_percent(self):
        self.percent += self.percent_speed/60

    def is_full_loading(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #faire une boucle de valeur entre 1 et 10
        for i in range (1, 10):
            #faire apparaitre un premiere boule de feu
            self.all_comet.add(Comet(self))

    def attempt_fall(self):
        #la jauge d'evenement est totalement charger
        if self.is_full_loading() and len(self.game.all_monster) == 0:
            print("pluie de comete")
            #faire apparaitre la pluie de comete
            self.meteor_fall()
            self.fall_mode = True #activer l'evenement



    def update_bar(self, surface):
        #ajouter du pourcentage a la barre
        self.add_percent()



        #creer la la barre d'evenment
        pygame.draw.rect(surface, (0,0,0), [
            0, #l'axe des x
            surface.get_height() - 10, #l'axe des y
            surface.get_width(), #longeur de la bar
            10 #largeur de la barre
        ])
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            (surface.get_height() - 10),  # l'axe des y
             (surface.get_width()/100)*self.percent,  # longeur de la bar
            10  # largeur de la barre
        ])


