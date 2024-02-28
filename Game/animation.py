import pygame

#definir une classe qui va s'occuper des animation
class animate_sprite(pygame.sprite.Sprite):

    def __init__(self, sprite_name):
        super().__init__()
        self.image = pygame.image.load(f'assets/{sprite_name}.png')
        self.current_image = 0 #commencer l'animation a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #definir une methode qui va demarrer l'animation
    def start_animation(self):
        self.animation = True

    #definir une methode pour animer le sprite
    def animate(self, loop=False):
        if self.animation:
            #passer a l'image suivantes
            self.current_image += 1
            #verifier si on atteint la fin de l'animation
            if self.current_image >= len(self.images):
                self.current_image = 0
                if loop is False:
                    #desactivation de l'animation
                    self.animation = False

            #modifier l'image precedente par la suivante
            self.image = self.images[self.current_image]



#definir une fonction qui va charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images de ce sprite dans le dossier correspondant
    images = []

    #recuperer le chemin du dossier pour se sprite
    path = f"assets/{sprite_name}/{sprite_name}"

    #boucler sur chaque image dans ce dossier pour les ajouter a la liste
    for num in range(1, 24):
        image_path = path + str(num) + ".png"
        images.append(pygame.image.load(image_path))
        print(image_path)
    #renvoyer le contenu de la liste d'images
    return images


#definir un dictionnaire qui va contenir les images charger de chaque listes
animations = {
    "mummy": load_animation_images("mummy"),
    "player": load_animation_images("player")

}
