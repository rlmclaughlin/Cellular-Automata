    
import pygame, random
import sys
import random
 
BLUE = (0, 0, 255)
WHITE = (255, 255, 255)
GREEN = (  0, 255,   0)

starting_margins = 5
square_size_w_padding = 22
border = 2
num_squares = 25 if len(sys.argv) == 1 else int(sys.argv[1])
WIN_SIZE =  square_size_w_padding * num_squares

curr_states =[ [random.randint(0,1)  for n in range(num_squares)] for i in range(num_squares)]
for i in curr_states:
    print (i)
next_states = [[0 for n in range(num_squares)] for i in range(num_squares)]

pygame.init()
 
size = (WIN_SIZE + (2 * starting_margins), WIN_SIZE + (2 * starting_margins))
screen = pygame.display.set_mode(size)

pygame.display.set_caption("Game of Life")
 
end_of_life = False
 
clock = pygame.time.Clock()
 
while not end_of_life:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            end_of_life = True
 
    locals=[-1, 0, 1]
    for i in range(len(curr_states)):
        for node in range(len(curr_states[i])):
            count = 0
            for j in locals:
                for k in locals:
                    if i + j >= 0 and i + j < num_squares and node + k >= 0 and node + k < num_squares and curr_states[(i + j)][(node + k)] == 1:
                        count += 1
            if curr_states[i][node] == 1:
                count -= 1
                if count < 2 or count > 3:
                    next_states[i][node] = 0
                else:
                    next_states[i][node] = 1
            else:
                if count == 3:
                    next_states[i][node] = 1
                else:
                    next_states[i][node] = 0

    for i in range(len(next_states)):
        for node in range(len(next_states[i])):
            curr_states[i][node] = next_states[i][node]
    
    screen.fill(GREEN)
     
    x= starting_margins
    while x < WIN_SIZE:
        y= starting_margins
        while y < WIN_SIZE:
            COLOR = BLUE if curr_states[int((x - starting_margins)/square_size_w_padding)][int((y-starting_margins)/square_size_w_padding)] == 0 else WHITE
    
            pygame.draw.rect(screen, COLOR, pygame.Rect(x, y, (square_size_w_padding - border), (square_size_w_padding - border)) )
            y += square_size_w_padding
        x += square_size_w_padding
    pygame.display.flip()
    clock.tick(5)
pygame.quit()