import pygame

class Game:
    def __innit__(self):
        self.running = True
        self.playing = False
        self.count = 0
        self.update_freq = 10

        self.positions = set()

        self.key_actions = {
            pygame.K_SPACE: self.toggle_play,
            pygame.K_c: self.clear_grid,
            pygame.K_g: self.randomize,
            pygame.K_1: self.place_four_gliders,
            pygame.K_w: self.place_glider_ur,
            pygame.K_a: self.place_glider_ul,
            pygame.K_s: self.place_glider_dl,
            pygame.K_d: self.place_glider_dr
        }

    def handle_keydown(self, key):
        action = self.key_actions.get(key)
        if action:
            action()

        def toggle_play(self):
            self.playing = not self.playing

    def clear_grid(self):
        self.positions.clear()
        self.playing = False
        self.count = 0

    def randomize(self):
        self.positions.clear()
        self.positions.update(
            gen(random.randrange(16, 24) * GRID_WIDTH)
        )

    def place_four_gliders(self):
        mx, my = pygame.mouse.get_pos()
        col = mx // TILE_SIZE
        row = my // TILE_SIZE
        self.positions.update(
            four_glider_collide((col, row))
        )

    def place_glider_dr(self):
        mx, my = pygame.mouse.get_pos()
        col = mx // TILE_SIZE
        row = my // TILE_SIZE
        self.positions.update(
            glider_dr((col, row))
        )
