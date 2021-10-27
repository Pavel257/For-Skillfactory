import sys

import pygame
import sys


def check_win(mas, sign):
    zeroes = 0
    for row in mas:
        zeroes += row.count(0)
        if row.count(sign) == 3:
            return sign
    for col in range(3):
        if mas[0][col] == sign and mas[1][col] == sign and mas[2][col] == sign:
            return sign
    if mas[0][0] == sign and mas[1][1] == sign and mas[2][2] == sign:
        return sign
    if mas[0][2] == sign and mas[1][1] == sign and mas[2][0] == sign:
        return sign
    if zeroes == 0:
        return 'Ничья'
    return False


pygame.init()

size = (490, 490)
margin = 10
width = heigth = 150
screen = pygame.display.set_mode(size)
pygame.display.set_caption("Крестики-нолики")

red = (255, 0, 0)
black = (0, 0, 0)
green = (0, 255, 0)
white = (255, 255, 255)
mas = [[0] * 3 for i in range(3)]
query = 0
game_over = False
while True:
    for event in pygame.event.get():

        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)
        elif event.type == pygame.MOUSEBUTTONDOWN and not game_over:
            x_mouse, y_mouse = pygame.mouse.get_pos()
            print(f' x={x_mouse}  y={y_mouse}')
            column = x_mouse // (margin + width)
            row = y_mouse // (margin + heigth)
            # mas[row][column] = mas[row][column] ^ 1
            if mas[row][column] == 0:
                if query % 2 == 0:
                    mas[row][column] = 'x'
                else:
                    mas[row][column] = 'o'
                query += 1
        elif event.type == pygame.KEYDOWN and event.key == pygame.K_SPACE:
            game_over = False
            mas = [[0] * 3 for i in range(3)]
            query = 0
            screen.fill(black)
    if not game_over:
        for row in range(3):
            for col in range(3):
                if mas[row][col] == 'x':
                    color = red
                elif mas[row][col] == 'o':
                    color = green
                else:
                    color = white
                x = col * width + (col + 1) * margin
                y = row * heigth + (row + 1) * margin
                pygame.draw.rect(screen, color, (x, y, width, heigth))
                if color == red:
                    pygame.draw.line(screen, white, (x + 15, y + 15), (x + width - 15, y + heigth - 15), 25)
                    pygame.draw.line(screen, white, (x + width - 15, y + 15), (x + 15, y + heigth - 15), 25)
                elif color == green:
                    pygame.draw.circle(screen, white, (x + width // 2, y + heigth // 2), (width + heigth) // 4 - 15, 25)
    if (query - 1) % 2 == 0:
        game_over = check_win(mas, 'x')

    else:
        game_over = check_win(mas, 'o')

    if game_over:
        screen.fill(black)
        font = pygame.font.SysFont('stxingkai', 200)
        text1 = font.render(game_over, True, white)
        text_rect = text1.get_rect()
        text_x = screen.get_width() / 2 - text_rect.width / 2
        text_y = screen.get_height() / 2 - text_rect.height / 2
        screen.blit(text1, [text_x, text_y])
    pygame.display.update()
