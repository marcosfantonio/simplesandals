import random
import time
import pygame
from pygame.locals import K_RETURN

import enemy_sprites
import player_sprites
import interface_sprites
import background_sprites

pygame.init()
game_end = False
running = True
arcade_font = pygame.font.Font("font/FONT.TTF", 48)

player_one_name = input("NAME OF THE FIRST PLAYER : ")
player_two_name = input("NAME OF THE SECOND PLAYER : ")


# Jogador
class Character:
    def __init__(self, name, health, attack, defense, x, y, displacement_front, displacement_backwards, sprite):
        # Atributos do Jogador
        self.name = name
        self.sprite = sprite
        self.max_health = health
        self.current_health = self.max_health
        self.attack = attack
        self.defense = defense
        self.x = x
        self.y = y
        self.original_x = x
        # Movimentação depois do ataque
        self.displacement_front = displacement_front
        self.displacement_backwards = displacement_backwards
        # Sons
        self.attack_1 = pygame.mixer.Sound("sounds/sword.mp3")
        self.hurt_sound = pygame.mixer.Sound("sounds/hurt.mp3")
        # Condições para as animações
        self.done = False
        self.action_index = 3
        self.action = None
        self.is_idle = True
        self.is_light_attacking = False
        self.is_heavy_attacking = False
        self.is_blocking = False
        self.is_desblocking = False
        self.is_idle_blocking = False
        self.collision_hit = False
        self.has_been_attacked = False
        self.is_dead = False

    # Função que desenha a barra de vida
    def draw_health_bar(self, screen, position):
        empty_rect = pygame.Rect(position[0], position[1], 426, 50)
        pygame.draw.rect(screen, (75, 75, 75), empty_rect)
        health_percentage = max(0, self.current_health / self.max_health)
        bar_width = int(health_percentage * 426)
        health_bar_rect = pygame.Rect(position[0], position[1], bar_width, 50)
        pygame.draw.rect(screen, (255, 0, 0), health_bar_rect)
    # Função que desenha o nome do personagem

    def draw_name(self, screen, position):
        name_text = arcade_font.render(self.name, True, (255, 255, 255))
        screen.blit(name_text, position)

    # Função que desenha o ícone de ações do personagem
    def draw_action(self, screen, position):
        if self.action == "light":
            self.action_index = 0
        elif self.action == "null":
            self.action_index = 3
        elif self.action == "heavy":
            self.action_index = 1
        elif self.action == "block":
            self.action_index = 2
        screen.blit(interface_sprites.action_sprites[self.action_index], position)

    # Função que desenha o personagem
    def draw_character(self, screen):
        if self.is_idle and not self.is_dead:
            self.idle()
            screen.blit(self.sprite.idle[self.sprite.idle_frame], (self.x, self.y))
        elif self.is_blocking:
            self.block_start()
            screen.blit(self.sprite.block_start[self.sprite.block_start_frame], (self.x, self.y))
        elif self.is_idle_blocking:
            self.block_idle()
            screen.blit(self.sprite.block_idle[self.sprite.block_idle_frame], (self.x, self.y))
        elif self.is_desblocking:
            self.desblock()
            screen.blit(self.sprite.desblock[self.sprite.desblock_frame], (self.x, self.y))
        elif self.is_light_attacking:
            self.light_attack()
            screen.blit(self.sprite.light_attack[self.sprite.light_attack_frame], (self.x, self.y))
        elif self.is_heavy_attacking:
            self.heavy_attack()
            screen.blit(self.sprite.heavy_attack[self.sprite.heavy_attack_frame], (self.x, self.y))
        elif self.has_been_attacked and not self.is_dead:
            self.hurt()
            screen.blit(self.sprite.hurt[self.sprite.hurt_frame], (self.x, self.y))
        elif self.is_dead:
            self.death()
            screen.blit(self.sprite.death[self.sprite.death_frame], (self.x, self.y))

    def idle(self):
        if self.is_idle:
            self.sprite.idle_frame += 1
            if self.sprite.idle_frame >= len(self.sprite.idle):
                self.sprite.idle_frame = 0

    def block_start(self):
        self.is_idle = False
        self.is_blocking = True
        if self.is_blocking:
            self.sprite.block_start_frame += 1
            if self.sprite.block_start_frame >= len(self.sprite.block_start):
                self.sprite.block_start_frame = 0
                self.is_blocking = False
                self.is_idle_blocking = True

    def block_idle(self):
        self.is_idle_blocking = True
        if self.is_idle_blocking:
            self.sprite.block_idle_frame += 1
            if self.sprite.block_idle_frame >= len(self.sprite.block_idle):
                self.sprite.block_idle_frame = 0

    def desblock(self):
        if self.is_desblocking:
            self.sprite.desblock_frame += 1
            if self.sprite.desblock_frame >= len(self.sprite.desblock):
                self.sprite.desblock_frame = 0
                self.is_desblocking = False
                self.is_idle = True

    def light_attack(self):
        self.is_idle = False
        self.is_light_attacking = True
        if self.is_light_attacking:
            self.sprite.light_attack_frame += 1
            if 1 <= self.sprite.light_attack_frame <= 3:
                self.x += self.displacement_front
                self.attack_1.play()
            if self.sprite.light_attack_frame == 3:
                self.collision_hit = True
            if self.sprite.light_attack_frame == 4:
                self.collision_hit = False
            if self.sprite.light_attack_frame >= 7:
                self.x -= self.displacement_backwards
            if self.sprite.light_attack_frame >= len(self.sprite.light_attack):
                self.sprite.light_attack_frame = 0
                self.is_light_attacking = False
                self.done = True
                self.is_idle = True
                self.x = self.original_x

    def heavy_attack(self):
        self.is_idle = False
        self.is_heavy_attacking = True
        if self.is_heavy_attacking:
            self.sprite.heavy_attack_frame += 1
            if 1 <= self.sprite.heavy_attack_frame <= 3:
                self.x += self.displacement_front
            if self.sprite.heavy_attack_frame == 5:
                self.attack_1.play()
            if self.sprite.heavy_attack_frame == 7:
                self.collision_hit = True
            if self.sprite.heavy_attack_frame == 8:
                self.collision_hit = False
            if self.sprite.heavy_attack_frame >= 11:
                self.x -= self.displacement_backwards
            if self.sprite.heavy_attack_frame >= len(self.sprite.heavy_attack):
                self.sprite.heavy_attack_frame = 0
                self.is_heavy_attacking = False
                self.done = True
                self.is_idle = True
                self.x = self.original_x

    def hurt(self):
        self.is_idle = False
        self.sprite.hurt_frame += 1
        if self.sprite.hurt_frame == 2:
            self.hurt_sound.play()
        if self.sprite.hurt_frame >= len(self.sprite.hurt):
            self.sprite.hurt_frame = 0
            self.has_been_attacked = False
            self.is_idle = True

    def death(self):
        self.is_idle = False
        self.sprite.death_frame += 1
        if self.sprite.death_frame >= len(self.sprite.death):
            self.sprite.death_frame = 6

    def handle_actions(self):
        if self.action == "light":
            self.light_attack()
        elif self.action == "heavy":
            self.heavy_attack()
        elif self.action == "block":
            self.block_start()


# Classe que executa as interações entre as outras classes
class Main:
    def __init__(self):
        # Atributos do Pygame
        self.clock = pygame.time.Clock()
        self.screen_size = [1280, 720]
        self.screen = pygame.display.set_mode(self.screen_size)
        self.turn = 0
        pygame.display.set_caption("Espadas e Sandálias")
        # Criação de objetos usando as classes
        self.player_one = Character(player_one_name, 100, 10, 50, -200, 125, 150, 100, player_sprites)
        self.player_two = Character(player_two_name, 100, 10, 50, 500, 125, -150, -100, enemy_sprites)
        # Sons
        self.fight_start = pygame.mixer.Sound("sounds/fight_start.mp3")
        self.music = pygame.mixer.Sound("sounds/ambience.mp3")
        self.victory = pygame.mixer.Sound("sounds/victory.mp3")
        self.select_sound = pygame.mixer.Sound("sounds/select.mp3")

    # Cenário
    def draw_background(self):
        self.screen.blit(background_sprites.background_sprites[background_sprites.background_index], (0, 0))
        background_sprites.background_index += 1
        if background_sprites.background_index >= len(background_sprites.background_sprites):
            background_sprites.background_index = 0

    # Elementos
    def draw_elements(self):
        self.draw_background()
        self.player_one.draw_character(self.screen)
        self.player_two.draw_character(self.screen)
        if battle_started:
            self.player_one.draw_action(self.screen, (265, 250))
            self.player_two.draw_action(self.screen, (950, 175))
            self.player_one.draw_health_bar(self.screen, (25, 25))
            self.player_two.draw_health_bar(self.screen, (829, 25))
            self.player_one.draw_name(self.screen, (50, 25))
            self.player_two.draw_name(self.screen, (854, 25))

    def play_music(self):
        self.music.play(-1)
        print("Music playing")

    def player_one_turn(self):
        if not self.player_two.is_dead:
            self.player_one.handle_actions()
            self.player_one.action = "null"
            self.player_two.action = "null"
            self.turn = 1

    def player_two_turn(self):
        if not self.player_one.is_dead:
            self.player_two.handle_actions()
            self.player_one.action = "null"
            self.player_two.action = "null"
            self.turn = 0

    @staticmethod
    def damage_formula(attack_type, player, target):
        attack_type = attack_type
        if attack_type == 0:
            crit_chance = 0.2
            crit_random = random.random()
            if crit_random < crit_chance:
                print("CRITICAL HIT")
                damage = player.attack * 2.5
                print(f"light attack damage : {damage}")
                return damage
            else:
                print("not crit")
                damage = player.attack
                print(f"light attack damage : {damage}")
                return damage
        elif attack_type == 1:
            damage = player.attack * 1.5
            print(f"heavy attack damage: {damage}")
            return damage
        elif attack_type == 3:
            damage = player.attack - target.defense
            if damage <= 0:
                damage = 0
            print(f"blocked attack damage: {damage}")
            return damage

    def register_fight(self):
        if ((self.player_one.is_light_attacking or self.player_one.is_heavy_attacking)
                and self.player_one.collision_hit):
            formula = int
            if self.player_one.is_light_attacking:
                formula = 0
            elif self.player_one.is_heavy_attacking:
                formula = 1
            if self.player_two.is_idle_blocking:
                damage = self.damage_formula(formula, self.player_one, self.player_two)
                self.player_two.current_health -= damage
                self.player_two.is_idle_blocking = False
                self.player_two.is_desblocking = True
            else:
                damage = self.damage_formula(formula, self.player_one, self.player_two)
                self.player_two.current_health -= damage
                if self.player_two.current_health <= 0:
                    self.player_two.has_been_attacked = True
                    self.player_two.hurt()
                    self.player_two.is_dead = True
                    self.player_two.death()
                    self.victory.play()
                else:
                    self.player_two.has_been_attacked = True
                    self.player_two.hurt()
        elif ((self.player_two.is_light_attacking or self.player_two.is_heavy_attacking)
              and self.player_two.collision_hit):
            formula = int
            if self.player_two.is_light_attacking:
                formula = 0
            elif self.player_two.is_heavy_attacking:
                formula = 1
            if self.player_one.is_idle_blocking:
                damage = self.damage_formula(formula, self.player_two, self.player_one)
                self.player_one.current_health -= damage
                self.player_one.is_idle_blocking = False
                self.player_one.is_desblocking = True
            else:
                damage = self.damage_formula(formula, self.player_two, self.player_one)
                self.player_one.current_health -= damage
                if self.player_one.current_health <= 0:
                    self.player_one.has_been_attacked = True
                    self.player_one.hurt()
                    self.player_one.is_dead = True
                    self.player_one.death()
                    self.victory.play()
                else:
                    self.player_one.has_been_attacked = True
                    self.player_one.hurt()


main = Main()
battle_started = False
blink_timer = 0
blint_interval = 0.5
show_text = True

main.play_music()
# Loop principal do pygame com métodos que estarão ativos sempre
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            # Detecta as teclas pressionadas
            if event.key == K_RETURN and not battle_started:
                battle_started = True
                print("Battle started")
                main.fight_start.play()
            if event.key == pygame.K_z and battle_started:
                main.player_one.action = "light"
                print("Player 1 Chooses Light Attack")
                main.select_sound.play()
            if event.key == pygame.K_x and battle_started:
                main.player_one.action = "heavy"
                print("Player 1 Chooses Heavy Attack")
                main.select_sound.play()
            if event.key == pygame.K_c and battle_started:
                main.player_one.action = "block"
                print("Player 1 Chooses Block")
                main.select_sound.play()
            if event.key == pygame.K_i and battle_started:
                main.player_two.action = "light"
                print("Player 2 Chooses Light Attack")
                main.select_sound.play()
            if event.key == pygame.K_o and battle_started:
                main.player_two.action = "heavy"
                print("Player 2 Chooses Heavy Attack")
                main.select_sound.play()
            if event.key == pygame.K_p and battle_started:
                main.player_two.action = "block"
                print("Player 2 Chooses Block")
                main.select_sound.play()
            if event.key == pygame.K_SPACE and battle_started and not game_end:
                if main.turn == 0 and main.player_one.action != "null":
                    print("Action confirmed on player one turn")
                    main.player_one_turn()
                elif main.turn == 1 and main.player_two.action != "null":
                    print("Action confirmed on player two turn")
                    main.player_two_turn()

    main.screen.fill((25, 0, 25))
    main.register_fight()
    main.draw_elements()
    if main.player_one.is_idle_blocking and main.player_two.is_idle_blocking:
        print("no action ocurred")
        main.player_one.is_idle_blocking = False
        main.player_one.is_desblocking = True
        main.player_two.is_idle_blocking = False
        main.player_two.is_desblocking = True
    if not battle_started:
        if time.time() - blink_timer > blint_interval:
            show_text = not show_text
            blink_timer = time.time()
        if show_text:
            text = arcade_font.render("Press Enter to start the battle", True, (255, 255, 255))
            main.screen.blit(text, (280, 200))
    if main.player_one.is_dead or main.player_two.is_dead:
        game_end = True
        if main.player_one.is_dead:
            text = arcade_font.render(f"{main.player_two.name} has won the battle!", True, (255, 255, 255))
            main.screen.blit(text, (280, 200))
            main.victory.play(-1)
        elif main.player_two.is_dead:
            text = arcade_font.render(f"{main.player_one.name} has won the battle!", True, (255, 255, 255))
            main.screen.blit(text, (280, 200))
            main.victory.play(-1)
    pygame.display.flip()
    main.clock.tick(10)
