# Readme
This is a creation of Conway's Game of Life. 
It is a cellular automaton that is played on a 2D square grid. Each square (or "cell") on the grid can be either alive or dead, and they evolve according to the following rules:
- Any live cell with fewer than two live neighbours dies (referred to as underpopulation).
- Any live cell with more than three live neighbours dies (referred to as overpopulation).
- Any live cell with two or three live neighbours lives, unchanged, to the next generation.
- Any dead cell with exactly three live neighbours comes to life. (https://conwaylife.com/)


My version of the game involves a few presets, pause and play, clear, generate noise, and change colour. The controls are as follows:

space - Pause/Play
c - clear
g - generate noise
r - change colour
w - north west moving glider
a - north east moving glider
s - south east moving glider
d - south west moving glider
1 - four glider collision
2 - breadcrumb grenade
3 - two ring explosive
4 - canada goose 
5 - acorn grenade
6 - copperhead (glider)
7 - space filler


# DOCS
This is creatd using pygame. 

While I believe the code is pretty self explanitory, there are a few things to be aware about. 

## coordinates
It is important to remember that x,y = 0,0 is at the top left corner, rather than the bottom left or the center. This means negative changes to y draws higher up the screen.

## draw_grid
This function is used to draw the updated grid with all 'positions'. Positions are a set of the locations for the live cells, you can think of positions as cells.

## adjust_grid
This function is used to step into the next generation of the programme. I.E. It checks the neighbours of all active positions and decides whether or not the position should be added to the new set of positions (kept alive). It then checks the neighbours of the 8 surrounding cells locations, whether active or not.
It then decides whether the cell is added to the new set of positions (stays alive or born) or not (dead or not spawned in).

## draw_set and draw_sets
These functions return the selected positions from the presets. draw_set simply adds each cell to the position from the given set, draw_set does the same but for eacah list in 'sets'. The functions these methods are used in (e.g soace_filler or acorn) are used with the built in update() function. 
This adds the new positions to the exisiting positions set, without removing the other exisiting positions.

## presets
The presets are broken down into key components, for example in space_filler, the preset is broken into left_wing, right_wing, left_feeler and so on. These segments are then broken down more where necessary, into smaller parts. All of these parts are distinguishable when looking at the drawn preset. The breakdowns allow for more maintanibility. It is easier to locate bugs and fix them.

## colours
The colours chosen are based of the blue, then using [OKLAB](https://oklch.com/#0.7,0.1,260,100), I was able to keep the lightness and chroma the same when choosing new colours, while only changing the hue. This makes the colour changes easier on the eye, and keeps the same feel. 

