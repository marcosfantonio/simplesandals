import pygame

action_size = [50, 50]
action_index = 0
action_sprites = [
    pygame.transform.scale(pygame.image.load("sprites/interface/light.png"), action_size),
    pygame.transform.scale(pygame.image.load("sprites/interface/heavy.png"), action_size),
    pygame.transform.scale(pygame.image.load("sprites/interface/shield.png"), action_size),
    pygame.transform.scale(pygame.image.load("sprites/interface/omo.png"), action_size)
]