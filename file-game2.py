import pygame
import sys
import math
import time

pygame.init()

WIDTH, HEIGHT = 800, 600
FPS = 60
PLAYER_RADIUS = 15
PLAYER_MOVE_DISTANCE = 3
BARRIER_COLOR = (0, 255, 0)
PLAYER_COLOR = (255, 255, 0)
BACKGROUND_COLOR = (0, 0, 0)
GAME_OVER_COLOR = (255, 0, 0)
U_IS_MOVING_FLAG = 0
D_IS_MOVING_FLAG = 0
L_IS_MOVING_FLAG = 0
R_IS_MOVING_FLAG = 0

screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Pac-Man Style Game")

player_pos = [WIDTH // 1.98, HEIGHT // 1.5]
direction = [0, 0]

# Барьеры (прямоугольники)
barriers = [
    pygame.Rect(0, 0, 800, 10),
    pygame.Rect(0, 0, 10, 270),
    pygame.Rect(0, 330, 10, 290),
    pygame.Rect(0, 590, 800, 10),
    pygame.Rect(790, 0, 10, 270),
    pygame.Rect(790, 330, 10, 290),
    pygame.Rect(51, 50, 324, 10),
    pygame.Rect(424, 50, 325, 10),
    pygame.Rect(51, 50, 10, 150),
    pygame.Rect(424, 50, 10, 150),
    pygame.Rect(51, 200, 324, 10),
    pygame.Rect(424, 200, 325, 10),
    pygame.Rect(370, 50, 10, 160),
    pygame.Rect(739, 50, 10, 150),

    pygame.Rect(51, 399, 324, 10),
    pygame.Rect(424, 399, 325, 10),
    pygame.Rect(51, 399, 10, 149),
    pygame.Rect(424, 399, 10, 139),
    pygame.Rect(424, 538, 325, 10),
    pygame.Rect(53, 538, 324, 10),
    pygame.Rect(370, 399, 10, 149),
    pygame.Rect(424, 399, 10, 139),
    pygame.Rect(739, 399, 10, 149),
]

def check_collision(player_pos):
    player_rect = pygame.Rect(player_pos[0] - (PLAYER_RADIUS * 1.3), player_pos[1] - (PLAYER_RADIUS * 1.3),
                               PLAYER_RADIUS * 2 * 1.3, PLAYER_RADIUS * 2 * 1.3)
    for barrier in barriers:
        if player_rect.colliderect(barrier):
            return True
    return False

def checking(player_pos, direction, PLAYER_MOVE_DISTANCE):
    player_pos2 = []
    player_pos2.append(player_pos[0] + direction[0] * PLAYER_MOVE_DISTANCE)
    player_pos2.append(player_pos[1] + direction[1] * PLAYER_MOVE_DISTANCE)
    return player_pos2

def main():
    clock = pygame.time.Clock()
    game_over = False
    global direction
    global PLAYER_MOVE_DISTANCE
    global player_pos
    global U_IS_MOVING_FLAG
    global D_IS_MOVING_FLAG
    global L_IS_MOVING_FLAG
    global R_IS_MOVING_FLAG
    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN and not game_over:
                if event.key == pygame.K_w and U_IS_MOVING_FLAG == 0:
                    if direction != [0, -1]:
                        PLAYER_MOVE_DISTANCE = 3
                    if not check_collision(checking(player_pos, [0, -1], 5)):
                        direction = [0, -1]
                        D_IS_MOVING_FLAG = 0
                        L_IS_MOVING_FLAG = 0
                        U_IS_MOVING_FLAG = 0
                        R_IS_MOVING_FLAG = 0
                elif event.key == pygame.K_s and D_IS_MOVING_FLAG == 0:
                    if direction != [0, 1]:
                        PLAYER_MOVE_DISTANCE = 3
                    if not check_collision(checking(player_pos, [0, 1], 5)):
                        direction = [0, 1]
                        D_IS_MOVING_FLAG = 0
                        L_IS_MOVING_FLAG = 0
                        U_IS_MOVING_FLAG = 0
                        R_IS_MOVING_FLAG = 0
                elif event.key == pygame.K_a and L_IS_MOVING_FLAG == 0:
                    if direction != [-1, 0]:
                        PLAYER_MOVE_DISTANCE = 3
                    if not check_collision(checking(player_pos, [-1, 0], 5)):
                        direction = [-1, 0]
                        D_IS_MOVING_FLAG = 0
                        L_IS_MOVING_FLAG = 0
                        U_IS_MOVING_FLAG = 0
                        R_IS_MOVING_FLAG = 0
                elif event.key == pygame.K_d and R_IS_MOVING_FLAG == 0:
                    if direction != [1, 0]:
                        PLAYER_MOVE_DISTANCE = 3
                    if not check_collision(checking(player_pos, [1, 0], 5)):
                        direction = [1, 0]
                        D_IS_MOVING_FLAG = 0
                        L_IS_MOVING_FLAG = 0
                        U_IS_MOVING_FLAG = 0
                        R_IS_MOVING_FLAG = 0
        if not game_over:
            player_pos2 = []
            player_pos2.append(player_pos[0] + direction[0] * PLAYER_MOVE_DISTANCE)
            player_pos2.append(player_pos[1] + direction[1] * PLAYER_MOVE_DISTANCE)
            if check_collision(player_pos2):
                PLAYER_MOVE_DISTANCE = 0
                if direction == [0, -1]:
                    U_IS_MOVING_FLAG = 1
                elif direction == [0, 1]:
                    D_IS_MOVING_FLAG = 1
                elif direction == [-1, 0]:
                    L_IS_MOVING_FLAG = 1
                elif direction == [1, 0]:
                    R_IS_MOVING_FLAG = 1
            else:
                player_pos = player_pos2
            if player_pos[0] < PLAYER_RADIUS:
                player_pos[0] = WIDTH - PLAYER_RADIUS
            elif player_pos[0] > WIDTH - PLAYER_RADIUS:
                player_pos[0] = PLAYER_RADIUS
        screen.fill(BACKGROUND_COLOR)
        for barrier in barriers:
            pygame.draw.rect(screen, BARRIER_COLOR, barrier)
        pygame.draw.circle(screen, PLAYER_COLOR, (int(player_pos[0]), int(player_pos[1])), PLAYER_RADIUS)
        if game_over:
            font = pygame.font.SysFont(None, 55)
            text_surface = font.render('Game Over', True, GAME_OVER_COLOR)
            text_rect = text_surface.get_rect(center=(WIDTH // 2, HEIGHT // 2))
            screen.blit(text_surface, text_rect)
        pygame.display.flip()
        clock.tick(FPS)

if __name__ == "__main__":
    main()
