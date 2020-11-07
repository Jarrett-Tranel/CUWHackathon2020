class Person(pygame.sprite.Sprite):
    
    def __init__(self, color, width, height):
        super().__init__()
        
        self.image = pygame.Surface([width, height])
        self.image.fill(WHITE)
        self.image.set_colorkey(WHITE)
 
        
        pygame.draw.rect(self.image, color, [0, 0, width, height])
        
        # Instead we could load an image of a person
        # self.image = pygame.image.load("person.png").convert_alpha()
 
        # Fetch the rectangle object that has the dimensions of the image.
        self.rect = self.image.get_rect()

pygame.init()
 

        

all_sprites_list = pygame.sprite.Group()
 
player = Person(RED, 40, 40)

player.rect.x = 200
player.rect.y = 300
 

all_sprites_list.add(player)
 


