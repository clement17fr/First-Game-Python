import pygame
from game import Game
import math
pygame.init()

pygame.display.set_caption("Comet Fall Game")
screen = pygame.display.set_mode((1080, 720))

clock = pygame.time.Clock()

background = pygame.image.load("assets/bg.jpg")

banner = pygame.image.load("assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil(screen.get_width()/4)
banner_rect.y = math.ceil(screen.get_height()/10)

play_button = pygame.image.load("assets/button.png")
play_button = pygame.transform.scale(play_button, (400, 150))
play_button_rect = play_button.get_rect()
play_button_rect.x = math.ceil(screen.get_width()/3.33)
play_button_rect.y = math.ceil(screen.get_height()/1.5)

restart_background = pygame.image.load("assets/game_over.jpg")
restart_background = pygame.transform.scale(restart_background, (1080,720))

replay_button = pygame.image.load("assets/restart.png")
replay_button = pygame.transform.scale(replay_button, (300, 220))
replay_button_rect = replay_button.get_rect()
replay_button_rect.x = math.ceil(screen.get_width()/2.7)
replay_button_rect.y = math.ceil(screen.get_height()/1.5)

game = Game()

running = True

while running:

    screen.blit(background, (0, -200))

    if game.is_playing:

        game.update(screen)

    else:
        if game.game_over_statut:
            if game.is_replaying:
                game.update(screen)
            else:
                screen.blit(restart_background, (0,0))
                screen.blit(replay_button,(replay_button_rect))
        else:
            screen.blit(banner, banner_rect)
            screen.blit(play_button, play_button_rect)


    pygame.display.flip()

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
            print("la fenetre est fermer")

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            if event.key == pygame.K_SPACE:
                game.player.launch_projectile()

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            if play_button_rect.collidepoint(event.pos):
                game.start()
            elif replay_button_rect.collidepoint(event.pos):
                game.start()

    clock.tick(60)



















