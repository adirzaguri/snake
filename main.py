import pygame
import pygame_menu
from snake import Snake
import constants
import  time 
from tkinter import *
from tkinter import messagebox
from random import randrange
from directions import Direction

def generate_apple(snake):
    apple = (randrange(0,19),randrange(0,19))
    while snake.in_body(apple):
        apple = (randrange(0,19),randrange(0,19))
    return apple

def draw_grid(snake,apple):
    screen.fill(constants.BLACK)
    for row in range(constants.Grid_rows):
        for column in range(constants.Grid_columns):
            color = constants.WHITE
            if (row,column) in snake.body:
                color = constants.GREEN
            if (row,column) == apple:
                color = constants.RED
            pygame.draw.rect(screen,
                             color,
                             [((constants.MARGIN + constants.WIDTH) * column + constants.MARGIN) ,
                              ((constants.MARGIN + constants.HEIGHT) * row + constants.MARGIN),
                              constants.WIDTH,
                              constants.HEIGHT])
    
    clock.tick(5*level)
    pygame.display.flip()


def set_difficulty(d,value):
    global level 
    level =value


def play(snake,apple):
    global score
    global level
    print(level)
    done = False
    # -------- Main Program Loop -----------
    while not done:
        for event in pygame.event.get():  # User did something
            if event.type == pygame.QUIT:  # If user clicked close
                done = True  # Flag that we are done so we exit this loop

            # The user changes the direction of the snake by pressing the matched key
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    snake.set_direction(Direction.LEFT)
                if event.key == pygame.K_UP:
                    snake.set_direction(Direction.UP)
                if event.key == pygame.K_RIGHT:
                    snake.set_direction(Direction.RIGHT)
                if event.key == pygame.K_DOWN:
                    snake.set_direction(Direction.DOWN)
        

    
        if snake.update():
            if apple == snake.head:
                snake.grow()
                apple = generate_apple(snake)
                score+=10
                level +=0.05    
        else: 
            messagebox.showinfo('Game Over',f'Game Over \n score :{score} ')
            pygame.quit()

        # Draw the map
        draw_grid(snake,apple)
    
    
        Tk().wm_withdraw() #to hide the main window
            
    pygame.quit()

# initialize the game's menu
def init_menu_and_run():
    menu = pygame_menu.Menu(300, 400, 'Welcome',
                       theme=pygame_menu.themes.THEME_DEFAULT)
    menu.add_text_input('Name :', default='guest')
    menu.add_selector('Difficulty :', [('Easy', 1),('Medium', 2),('Hard',3),('Extreme',10) ], onchange=set_difficulty)
    menu.add_button('Play', play,snake,apple)
    menu.add_button('Quit', pygame_menu.events.EXIT)

    menu.mainloop(screen)


# Initialize pygame
pygame.init()
screen = pygame.display.set_mode(constants.WINDOW_SIZE)
clock = pygame.time.Clock()
pygame.display.set_caption("Snake")


# Initialize game variables
snake = Snake([(1,6),(1,5)],Direction.RIGHT)
score = 0
apple = generate_apple(snake)
level = 1


if __name__ == '__main__':
    
    init_menu_and_run()
    #play(snake,apple)