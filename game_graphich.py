import pygame
import words_operations
import game_core
import random
import pygame_menu


pygame.init()

WIDTH, HEIGHT = 960, 560
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)


screen = pygame.display.set_mode((WIDTH, HEIGHT))

font = pygame.font.Font(None, 36)

options = ["Начать игру", "Выход"]


current_option = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                current_option = (current_option - 1) % len(options)
            elif event.key == pygame.K_DOWN:
                current_option = (current_option + 1) % len(options)
            elif event.key == pygame.K_RETURN:
                if options[current_option] == "Начать игру":
                   
                    print("Игра начинается...")
            
                elif options[current_option] == "Выход":
                    pygame.quit()
                    sys.exit()
animation_set = [pygame.image.load(f"r{i}.png") for i in range(1, 6)]

window = pygame.display.set_mode((640, 480))

clock = pygame.time.Clock()
i = 0
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    window.fill((0,0,0))
    window.blit(animation_set[i // 12], (100, 20))
    i += 1
    if i == 60:
        i = 0
   
    screen.fill(WHITE)
    for i, option in enumerate(options):
        color = BLACK
        if i == current_option:
            color = (255, 0, 0)
        text = font.render(option, True, color)
        screen.blit(text, (WIDTH // 2 - text.get_width() // 2, HEIGHT // 2 - text.get_height() // 2 + i * 50))

    pygame.display.flip()