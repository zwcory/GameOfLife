import random

import pygame


pygame.init()

BLACK = (10,10,10)
GREY = (128,128,128)
BLUE = (179,235,242)

BG = BLACK
LINE = GREY
CELL = BLUE


WIDTH, HEIGHT =  800,800
TILE_SIZE = 10
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for i in range(num)])


# 0,0 Is from top left, y increasing as we go down
def draw_grid(positions):
    for position in positions:
        col,row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, CELL, (*top_left, TILE_SIZE, TILE_SIZE))




    for row in range (GRID_HEIGHT):
        pygame.draw.line(screen, LINE, (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE))

    for col in range (GRID_WIDTH):
        pygame.draw.line(screen, LINE, (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT))







def main():
    running = True
    playing = True

    positions = set()

    positions.add((10,10))
    while running:
        clock.tick(FPS)

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            # add click to add or remove cell

            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    playing = not playing

                if event.key == pygame.K_c:
                    positions = set()
                    playing = False

                if event.key == pygame.K_g:
                    positions = gen(random.randrange(8,12) * GRID_WIDTH)




        screen.fill(BG)
        draw_grid(positions)
        pygame.display.update()

    pygame.quit()

if __name__ == "__main__":
    main()