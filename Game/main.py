import pygame
from game import Game
import math
pygame.init()

#creer une seconde classe qui va representer notre jeu

pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))

#affichage des image par seconde
clock = pygame.time.Clock()

#importer de charger l'image d'arriere plan
background = pygame.image.load("assets/bg.jpg")

#charger notre banniere
banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)
banner_rect.y = math.ceil(screen.get_height()/10)

#charger notre bouton pour lancer notre partie
play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/1.5)

#charger notre nouvel arriere plan
restart_background = pygame.image.load("assets/game_over.jpg")
restart_background = pygame.transform.scale(restart_background, (1080,720))


#charger notre bouton restart
replay_button = pygame.image.load("assets/restart.png")
replay_button = pygame.transform.scale(replay_button, (300, 220))
replay_button_rect = replay_button.get_rect()
replay_button_rect.x = math.ceil(screen.get_width()/2.7)
replay_button_rect.y = math.ceil(screen.get_height()/1.5)

#charger notre joueur
game = Game()

#boucle tant que cette condition est vrai
running = True

while running:
    # ajouter l'image a la fenetre
    screen.blit(background, (0, -200))

    if game.is_playing:
        #declencher les instruction de la partie
        game.update(screen)


    #verifier si notre jeu n'a pas commencer
    else:
        if game.game_over_statut:
            if game.is_replaying:
                game.update(screen)
            else:
                screen.blit(restart_background, (0,0))
                screen.blit(replay_button,(replay_button_rect))
        else:
        #ajouter mon ecran d'acceuil
            screen.blit(banner, banner_rect)
            screen.blit(play_button, play_button_rect)

    #mettre a jour l'image
    pygame.display.flip()

    #si le joueur ferme la fenetre
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("la fenetre est fermer")

        #detecter si un joueur lache une touche du clavier
        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #detecter si la touche espace est enclencher
            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifier si la souris est en collision avec le bouton jouer
            if play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancer
                game.start()
            elif replay_button_rect.collidepoint(event.pos):
                game.start()

    clock.tick(60)



















