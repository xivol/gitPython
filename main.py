import pygame
import math
BG_COLOR = pygame.Color('yellow')
RECT_COLOR = pygame.Color(128, 16, 16)
CIR_COLOR = pygame.Color(16, 128, 16)
LINE_COLOR = pygame.Color(16, 16, 128)

pygame.init()
size = width, height = 800, 600
screen = pygame.display.set_mode(size)
pygame.display.set_caption('MY SUPER GAME')

icon = pygame.Surface((32, 32))
pygame.draw.circle(icon, BG_COLOR, (16,16), 16)
pygame.display.set_icon(icon)

screen.fill(BG_COLOR)
screen.fill(RECT_COLOR, (400,0, 400, 600))

pygame.draw.rect(screen, RECT_COLOR, (100, 100,  150, 250), border_radius=16)
pygame.draw.circle(screen, CIR_COLOR, (100, 100), 75, width=8)
pygame.draw.ellipse(screen, CIR_COLOR, (250, 250,  100, 150))
pygame.draw.line(screen, LINE_COLOR, (175, 100), (450, 100), width=8)

n = 16
poly = []
for i in range(n):
    x = width // 2 + math.cos(i * 2 * math.pi / n) * 100
    y = width // 2 + math.sin(i * 2 * math.pi / n) * 100
    poly.append((x,y))

pygame.draw.lines(screen, LINE_COLOR, True, poly, width=8)
pygame.draw.polygon(screen, RECT_COLOR, poly)

pygame.display.flip()
while pygame.event.wait().type != pygame.QUIT:
    pass
#
pygame.quit()
