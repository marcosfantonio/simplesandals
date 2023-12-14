import pygame

# Parâmetros de Tamanho
health_bar_size = [256, 128]
size = [120 * 8, 60 * 8]

# Parado
idle_frame = 0
idle = [
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_4.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_5.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_6.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_7.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_6.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_7.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_idle_8.png"), size)
]

# Entrando no block
block_start_frame = 0
block_start = [
    pygame.transform.scale(pygame.image.load("sprites/player/player_blocking_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_blocking_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_blocking_2.png"), size)
]

# Saindo do block
desblock_frame = 0
desblock = [
    pygame.transform.scale(pygame.image.load("sprites/player/player_desblock_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_desblock_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_desblock_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_desblock_3.png"), size)
]

# Bloqueando
block_idle_frame = 0
block_idle = [
    pygame.transform.scale(pygame.image.load("sprites/player/player_is_blocking_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_is_blocking_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_is_blocking_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_is_blocking_3.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_is_blocking_4.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_is_blocking_5.png"), size),
]

# Ao levar dano
hurt_frame = 0
hurt = [
    pygame.transform.scale(pygame.image.load("sprites/player/player_hit_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_hit_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_hit_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_hit_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_hit_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_hit_2.png"), size),
]

# Ataque leve
light_attack_frame = 0
light_attack = [
    pygame.transform.scale(pygame.image.load("sprites/player/player_attack_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_attack_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_attack_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_attack_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_attack_3.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_attack_3.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_attack_4.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_attack_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_attack_1.png"), size),
]

# Ataque pesado
heavy_attack_frame = 0
heavy_attack = [
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_3.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_3.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_3.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_4.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_4.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_4.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_heavy_attack_2.png"), size),
]

# Morte
death_frame = 0
death = [
    pygame.transform.scale(pygame.image.load("sprites/player/player_death_0.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_death_1.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_death_2.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_death_3.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_death_4.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_death_5.png"), size),
    pygame.transform.scale(pygame.image.load("sprites/player/player_death_7.png"), size),
]
