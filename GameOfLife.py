import random

import pygame


pygame.init()
GREY = (128,128,128)

LINE = GREY


# bgs
ONE_BG = (2, 97, 106)
TWO_BG = (20, 99, 85)
THREE_BG = (56, 96, 59)
FOUR_BG = (63, 95, 53)
FIVE_BG = (86, 89, 35)
SIX_BG = (104, 81, 29)
SEVEN_BG = (117, 73, 41)
EIGHT_BG = (116, 67, 91)
NINE_BG = (103, 71, 112)




# cells
ONE = (179,235,242)
TWO = (183, 237, 223)
THREE = (200, 234, 201)
FOUR = (205, 233, 196)
FIVE = (224, 228, 184)
SIX = (241, 221, 180)
SEVEN = (255, 214, 188)
EIGHT = (255, 208, 229)
NINE = (241, 212, 249)



CELL_COLOURS = [ONE, TWO, THREE, FOUR, FIVE, SIX, SEVEN, EIGHT, NINE]
BG_COLOURS = [ONE_BG, TWO_BG, THREE_BG, FOUR_BG, FIVE_BG, SIX_BG, SEVEN_BG, EIGHT_BG, NINE_BG]

WIDTH, HEIGHT =  800,800
TILE_SIZE = 5
GRID_WIDTH = WIDTH // TILE_SIZE
GRID_HEIGHT = HEIGHT // TILE_SIZE
FPS = 60

screen = pygame.display.set_mode((WIDTH,HEIGHT))

clock = pygame.time.Clock()

def gen(num):
    return set([(random.randrange(0, GRID_HEIGHT), random.randrange(0, GRID_WIDTH)) for i in range(num)])

def randomize_colour():
    num = random.randrange(0,8)
    cell = CELL_COLOURS[num]
    bg = BG_COLOURS[num]

    return cell, bg


# 0,0 Is from top left, y increasing as we go down
def draw_grid(positions, cell_colour):
    for position in positions:
        col,row = position
        top_left = (col * TILE_SIZE, row * TILE_SIZE)
        pygame.draw.rect(screen, cell_colour, (*top_left, TILE_SIZE, TILE_SIZE))


    # Create transparent grid surface
    grid_surface = pygame.Surface((WIDTH, HEIGHT), pygame.SRCALPHA)

    # transparent_line = (*CELL, 40)
    transparent_line = (*LINE, 40)

    for row in range(GRID_HEIGHT):
        pygame.draw.line(
            grid_surface, transparent_line,
            (0, row * TILE_SIZE), (WIDTH, row * TILE_SIZE)
        )

    for col in range(GRID_WIDTH):
        pygame.draw.line(
            grid_surface, transparent_line,
            (col * TILE_SIZE, 0), (col * TILE_SIZE, HEIGHT)
        )

    # Blit the transparent grid on top of the screen
    screen.blit(grid_surface, (0, 0))


def adjust_grid(positions):
    all_neighbours = set()
    new_positions = set()

    for position in positions:
        neighbours = get_neighbours(position)
        all_neighbours.update(neighbours)


        # is neighbour(x) in positions (list of active cells), if it is keep it, if not remove it
        neighbours = list(filter(lambda x: x in positions, neighbours))

        # if length of neighbours is 2/3 add the position to new position
        # if it isn't ( len(neighbours) < 2 or len(neighbours)>3, it dies
        # so we don't add it to new position
        if len(neighbours) in [2,3]:
            new_positions.add(position)


    for position in all_neighbours:
        # get neighbours of neighbours (we don't need to check cells that don't have neighbours)
        neighbours = get_neighbours(position)
        neighbours = list(filter(lambda x: x in positions, neighbours))

        if len(neighbours) == 3:
            new_positions.add(position)

    return new_positions


def get_neighbours(pos):
    x,y = pos
    neighbours = []
    for dx in [-1,0,1]:
        if x + dx < 0 or x + dx >= GRID_WIDTH:
            continue
        for dy in [-1,0,1]:
            if y + dy < 0 or y + dy >= GRID_HEIGHT:
                continue
            # don't check 'pos', already has it and isn't a neighbour
            if dx == 0 and dy == 0:
                continue

            neighbours.append((x + dx, y + dy))
    return neighbours

""" PRESETS """
def four_glider_collide(position):
    # lower right glider (y increases going down
    lr_glider = [(5,3),(4,3),(3,3)
                ,(3,4),(4,5)]

    # lower left
    ll_glider = [(-5,3),(-4,3),(-3,3)
                ,(-3,4),(-4,5)]

    # upper right
    ur_glider = [(5,-2),(4,-2),(3,-2)
                ,(3,-3),(4,-4)]

    # upper left
    ul_glider = [(-5,-2),(-4,-2),(-3,-2)
                ,(-3,-3),(-4,-4)]

    gliders = [ul_glider, ur_glider, ll_glider, lr_glider]
    return draw_sets(position,gliders)

def bread_crumb_grenade(position):
    tl = [(-1,-3),(-1,-4),(-2,-4)
        ,(-3,-3),(-3,-2),(-2,-2)
        ,(0,-1)]

    tr = [(2,-3),(2,-4),(3,-4)
        ,(4,-3),(4,-2),(3,-2)
        ,(1,-1)]

    br = [(2,3),(2,4),(3,4)
        ,(4,3),(4,2),(3,2)
        ,(1,0)]

    bl = [(-1,3),(-1,4),(-2,4)
        ,(-3,3),(-3,2),(-2,2)
        ,(0,0)]

    segments = [bl,br,tl,tr]

    return draw_sets(position,segments)



def glider_ur(position):
    glider = [(0,0),(-1,0),(-2,0)
            ,(0,1) ,(-1,2)]
    return draw_set(position, glider)

def glider_dr(position):
    glider = [(0,0),(-1,0),(-2,0)
            ,(0,-1) ,(-1,-2)]
    return draw_set(position, glider)

def glider_dl(position):
    glider = [(0,0),(1,0),(2,0)
            ,(0,-1),(1,-2)]
    return draw_set(position, glider)

def glider_ul(position):
    glider = [(0,0),(1,0),(2,0)
            ,(0,1),(1,2)]
    return draw_set(position, glider)

def two_ring_explosive(position):
    left  = [(-3,-1),(-2,-1),(-1,-1),
              (-3,0),(-1,0),
             (-3,1), (-2,1),(-1,1)]
    right = [(3,-1),(2,-1),(1,-1),
             (3,0),(1,0),
             (3,1), (2,1),(1,1)]
    rings = [left,right]
    return draw_sets(position, rings)

def canada_goose(position):
    tl = [(-6,-5), (-5,-5), (-4,-5),
          (-6,-4), (-5,-3) ]

    ml = [(-3,-2), (-2,-2), (-2,-1)]

    tr = [(1,-2), (2,-2), (2,-3),
          (3,-3), (4,-3), (4,-4),
          (5,-4), (6,-3)]

    mr =[(2,0),(3,1)]

    lr = [(1,2), (2,2), (2,3),
          (2,4), (1,4), (4,3),
          (5,3)]

    ll = [(-1,3),(-1,2),(-1,1),
          (-2,1), (-3,2), (-3,3),
          (-4,4), (-4,5), (-4,6),
          (-3,5), (-3,6)]

    segments = [tl, ml, tr, mr, lr, ll]
    return draw_sets(position, segments)



def copper_head(position):
    tl = [(-3,-6),(-2,-6),(-1,-5),
          (-1,-4),(-2,-3),(-4,-3),
          (-4,-2)]

    tr = [(2,-6),(1,-6),(0,-5),
          (0,-4),(1,-3),(3,-3),
          (3,-2)]

    ll = [(-4,0),(-3,1),(-2,1),
          (-2,2),(-1,2),(-1,4),
          (-1,5)]

    lr = [(3,0),(2,1),(1,1),
          (1,2),(0,2),(0,4),
          (0,5)]

    segments = [tl,tr,ll,lr]
    return draw_sets(position,segments)

def space_filler(position):
    left_wing = [(-24,-11), (-23,-11), (-22,-11),
                 (-21,-11), (-24,-10), (-24,-9),
                 (-23,-8),(-20,-8),(-20,-10),

                 (-20,-4),(-20,-2),(-21,-1),
                 (-22,-1),(-23,-1),(-24,-1),
                 (-24,-2),(-24,-3),(-23,-4),

                 (-15,-9),(-13,-8),(-12,-7),
                 (-12,-6),(-12,-5),(-13,-4),
                 (-15,-3),(-16,-4),(-17,-4),
                 (-18,-5),(-18,-6),(-18,-7),
                 (-17,-8),(-16,-8)]

    right_wing = [(24,-11), (23,-11), (22,-11),
                  (21,-11), (24,-10), (24,-9),
                  (23,-8),(20,-8),(20,-10),

                  (20,-4),(20,-2),(21,-1),
                  (22,-1),(23,-1),(24,-1),
                  (24,-2),(24,-3),(23,-4),

                  (15,-9),(13,-8),(12,-7),
                  (12,-6),(12,-5),(13,-4),
                  (15,-3),(16,-4),(17,-4),
                  (18,-5),(18,-6),(18,-7),
                  (17,-8),(16,-8)]

    left_feeler = [(-2,-9),(-2,-10),(-2,-11),
                    (-2,-12),(-2,-13),(-3,-13),
                    (-4,-13),(-5,-12)]

    right_feeler = [(2,-9),(2,-10),(2,-11),
                   (2,-12),(2,-13),(3,-13),
                   (4,-13),(5,-12)]

    mid_left = [(-4,-7), (-3,-7), (-2,-7),
                (-3,-6), (-3,-5), (-2,-5),
                (-1,-5), (-4,-4), (-5,-3),
                (-4,-3), (-3,-3), (-2,-3),
                (-1,-3),

                (-10,-4), (-9,-4), (-11,-3),
                (-10,-3), (-10,-2), (-9,-2),
                (-9,-1), (-8,-1), (-8,0),
                (-7,-1), (-6,-1), (-6,0),
                (-5,-1), (-4,-1), (-3,-1),
                (-2,-1), (-1,-1)]

    mid_right = [(4,-7), (3,-7), (2,-7),
                 (3,-6), (3,-5), (2,-5),
                 (1,-5), (4,-4), (5,-3),
                 (4,-3), (3,-3), (2,-3),
                 (1,-3),

                 (10,-4), (9,-4), (11,-3),
                 (10,-3), (10,-2), (9,-2),
                 (9,-1), (8,-1), (8,0),
                 (7,-1), (6,-1), (6,0),
                 (5,-1), (4,-1), (3,-1),
                 (2,-1), (1,-1)]

    center_mid = [(0,-5),(0,-3),(0,-1),
                  (0,1),(0,3),(0,4)]

    lower_left = [(-5,2), (-5,1), (-4,1),
                  (-3,1), (-2,1), (-1,1),
                  (-4,3), (-3,3), (-2,3),
                  (-1,3), (-4,5), (-3,5),
                  (-2,5), (-2,6)]

    lower_right = [(5,2), (5,1), (4,1),
                  (3,1), (2,1), (1,1),
                  (4,3), (3,3), (2,3),
                  (1,3), (4,5), (3,5),
                  (2,5), (2,6)]

    bottom_left = [(-3,8), (-2,8), (-1,8),
                   (-1,9), (-1,10), (-2,11),
                   (-3,12), (-4,11), (-4,10),
                   (-3,9), (-2,9), (-2,10),
                   (-3,11)]

    bottom_right = [(3,8), (2,8), (1,8),
                    (1,9), (1,10), (2,11),
                    (3,12), (4,11), (4,10),
                    (3,9), (2,9), (2,10),
                    (3,11)]

    segments = [left_wing, right_wing, left_feeler, right_feeler, mid_left, mid_right, center_mid, lower_left, lower_right, bottom_left, bottom_right]
    return draw_sets(position,segments)

def acorn(position):
    shape = [(-3,0),(-2,0),(0,-1),
             (-2,-2),(1,0),(2,0),
             (3,0)]

    return draw_set(position, shape)

def draw_set(position, locations):
    positions = set()
    px, py = position
    x = px // TILE_SIZE
    y= py // TILE_SIZE

    for cell in locations:
        dx , dy = cell
        new_cell = x + dx,  y +dy
        positions.add(new_cell)

    return positions

def draw_sets(position, sets):
    positions = set()
    px, py = position
    x = px // TILE_SIZE
    y= py // TILE_SIZE

    for locations in sets:
        for cell in locations:
            dx , dy = cell
            new_cell = x + dx,  y +dy
            positions.add(new_cell)
    return positions




class Game:
    def __init__(self):
        self.running = True
        self.playing = False
        self.count = 0
        self.update_freq = 10
        self.CELL_COLOUR = ONE
        self.BG_COLOUR = ONE_BG


        self.positions = gen(random.randrange(16, 24) * GRID_WIDTH)

        self.key_actions = {
            pygame.K_SPACE: self.toggle_play,
            pygame.K_c: self.clear_grid,
            pygame.K_g: self.randomize,
            pygame.K_1: self.place_four_glider_collide,
            pygame.K_w: self.place_glider_ur,
            pygame.K_a: self.place_glider_ul,
            pygame.K_s: self.place_glider_dl,
            pygame.K_d: self.place_glider_dr,
            pygame.K_r: self.set_random_colour,
            pygame.K_2: self.place_breadcrumb_gren,
            pygame.K_3: self.place_two_ring,
            pygame.K_4: self.place_canada_goose,
            pygame.K_5: self.place_acorn,
            pygame.K_6: self.place_copperhead,
            pygame.K_7: self.place_space_filler,

        }

    # ---------- input ----------
    def handle_keydown(self, key):
        action = self.key_actions.get(key)
        if action:
            action()

    # ---------- actions ----------
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

    def place_four_glider_collide(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            four_glider_collide((col, row))
        )

    def place_glider_dr(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            glider_dr((col, row))
        )
    def place_glider_ur(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            glider_ur((col, row))
        )
    def place_glider_dl(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            glider_dl((col, row))
        )
    def place_glider_ul(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            glider_ul((col, row))
        )
    def set_random_colour(self):
        self.CELL_COLOUR, self.BG_COLOUR = randomize_colour()

    def place_breadcrumb_gren(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            bread_crumb_grenade((col, row))
        )

    def place_two_ring(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            two_ring_explosive((col, row))
        )

    def place_canada_goose(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            canada_goose((col, row))
        )

    def place_acorn(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            acorn((col, row))

        )

    def place_copperhead(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            copper_head((col, row))
        )

    def place_space_filler(self):
        col, row = self.mouse_to_pixel()
        self.positions.update(
            space_filler((col, row))
        )

    # ---------- helpers ----------
    def mouse_to_grid(self):
        mx, my = pygame.mouse.get_pos()
        return mx // TILE_SIZE, my // TILE_SIZE

    def mouse_to_pixel(self):
        return pygame.mouse.get_pos()

    # ---------- main loop ----------
    def run(self):
        while self.running:
            clock.tick(FPS)

            if self.playing:
                self.count += 1

            if self.count >= self.update_freq:
                self.count = 0
                self.positions = adjust_grid(self.positions)

            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.running = False

                elif event.type == pygame.KEYDOWN:
                    self.handle_keydown(event.key)

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    col, row = self.mouse_to_grid()
                    pos = (col, row)
                    if pos in self.positions:
                        self.positions.remove(pos)
                    else:
                        self.positions.add(pos)

            pygame.display.set_caption(
                "Playing" if self.playing else "Paused"
            )

            screen.fill(self.BG_COLOUR)
            draw_grid(self.positions, self.CELL_COLOUR)
            pygame.display.update()


# -------------------- entry point --------------------
def main():
    game = Game()
    game.run()
    pygame.quit()


if __name__ == "__main__":
    main()