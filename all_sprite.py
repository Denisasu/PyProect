
import pygame
from player import Player
from enemys import Dementor, Sova, Clans

all_sprites = pygame.sprite.Group()
bullets = pygame.sprite.Group()
player = Player()
all_sprites.add(player)
all_sprites.add(bullets)
enemy = pygame.sprite.Group()
death = pygame.sprite.Group()
dem = pygame.sprite.Group()
sov = pygame.sprite.Group()
cl = pygame.sprite.Group()
score = 0
for i in range(6):
    d = Dementor()
    s = Sova()
    c = Clans()
    dd = Pojirateli()
    all_sprites.add(d)
    all_sprites.add(s)
    all_sprites.add(c)
    all_sprites.add(dd)
    dem.add(d)
    sov.add(s)
    cl.add(c)
    death.add(dd)