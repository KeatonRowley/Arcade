import pygame
import random
from pygame.locals import *

# Image resources.
background_img_name = ".\Images\GrassBackground.jpg"

# color resources
BLACK = (0, 0, 0)
WHITE = (200, 200, 200)
RED = (255, 0, 0)
HEAD_COLOR = (224, 50, 70)
TAIL_COLOR = (14, 22, 77)
FOOD_COLOR = (7, 43, 66)

UP = (0,-1)
DOWN = (0, 1)
LEFT = (-1,0)
RIGHT = (1,0)


class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.blockSize = 20 # size of the grid
        self.board_size = self.gridWidth, self.gridHeight = 32, 20
        self.size = self.width, self.height = self.gridWidth*self.blockSize, self.gridHeight*self.blockSize
        self.clock = pygame.time.Clock()
        self.time_elapsed_since_last_action = 0
        self.gameInPlay = False
        self.levelMessage = "Press space to start game."
        self.init_game()
        self.curr_score = 0
        self.high_score = 0
    
        
    
    def init_game(self):
        self.food_pos = self.generate_loc()
        self.snake =  self.generate_start_snake(3, [self.food_pos])
        self.direction = self.generate_rand_dir()
        self.speed = 200  # number of milliseconds between updates.
        self.score = 0

    def on_init(self):
        pygame.init()
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF, pygame.HWSURFACE)
        self._running = True
        self.init_game()

        # Load background image
        self._image_surf = pygame.image.load(background_img_name).convert()
 
    # Calls proper 
    def on_event(self, event):
        if event.type == QUIT:
            self.on_exit()
 
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if self.gameInPlay is False:
                    self.gameInPlay = True

            elif event.key == pygame.K_UP:
                if self.direction != DOWN:
                    self.direction = UP
            elif event.key == pygame.K_DOWN:
                if self.direction != UP:
                    self.direction = DOWN 
            elif event.key == pygame.K_RIGHT:
                if self.direction != LEFT:
                    self.direction = RIGHT 
            elif event.key == pygame.K_LEFT:
                if self.direction != RIGHT:
                    self.direction = LEFT
                
    
    def on_loop(self):
        self._image_surf = pygame.image.load(background_img_name).convert()
        # updates the in play game, otherwise updates the waiting to play mode.
        if self.gameInPlay:
            self.check_snake()
            self.draw_snake()
            self.draw_box(self.food_pos, BLACK, self.blockSize)
            
        else:
            pygame.font.init()
            font = pygame.font.SysFont('Comic Sans MS', 20)
            text = font.render(self.levelMessage, True, RED)
            text_rect = text.get_rect()
            text_rect.center = (self.width //2, self.height //2 )
            self._image_surf.blit(text, text_rect)

    def on_render(self):
         # Display the score and high score.
        font = pygame.font.SysFont('Comic Sans MS', 20)
        text = font.render("Score: "+ str(self.curr_score) + "  High score: " + str(self.high_score), True, RED)
        text_rect = text.get_rect()
        text_rect.center = (self.width - 140, self.height // 20)
        self._image_surf.blit(text, text_rect)

        self._display_surf.blit(self._image_surf, (0,0))
       
        
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while( self._running ):
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
        self.on_cleanup()
    
    def on_exit(self):
        self._running = False
 
    
    # Helper methods.

    # If time has expired, updates the snake.
    def check_snake(self):
        dt = self.clock.tick()
        self.time_elapsed_since_last_action += dt

        if self.time_elapsed_since_last_action >= self.speed:
            self.time_elapsed_since_last_action = 0
            self.update_snake()

    # Check if position of the square is outside of the screen.
    def check_out_of_bounds(self, pos):
        out_of_bounds =  (
                pos[0] > self.gridWidth 
                or pos[0] < 0
                or pos[1] > self.gridHeight
                or pos[1] < 0
        )
        return out_of_bounds
    
    # Draw a single grid square on the screen.
    def draw_box(self, pos, color, mult, offset = 0):
            x, y = pos
            rect = pygame.Rect(x*mult, y*mult, self.blockSize, self.blockSize)
            pygame.draw.rect(self._image_surf, color, rect, offset)

    # Draw the entire screen crid.
    def draw_grid(self):
        for x in range(0, self.width, self.blockSize):
            for y in range(0, self.height, self.blockSize):
                self.draw_box((x, y), WHITE, 1, 1)
                

    def draw_snake(self):
        # draw head
        pos = self.snake[0]
        self.draw_box(pos, HEAD_COLOR, self.blockSize)
        # draw tail
        for pos in self.snake[1:]:
            self.draw_box(pos, TAIL_COLOR, self.blockSize)
        
    # Pick random (x, y) location inside the gridwidth. 
    def generate_loc(self):
        x = random.randint(0, self.gridWidth-1)
        y = random.randint(0, self.gridHeight-1)
        return (x, y)
    
    def generate_rand_dir(self):
        directions = [LEFT, RIGHT, UP, DOWN]
        choice = random.randint(0, 3)
        return directions[choice]


    def game_over(self):
        self.gameInPlay = False
        self.levelMessage = "Game over (press space to play again)."
        self.speed = 200
        
        # Check for high score update.
        if self.curr_score > self.high_score:
            self.high_score = self.score

        self.init_game()


    def generate_start_snake(self, start_len, forbidden_coor):
        head_pos = self.generate_loc()

        #Generate positions not already picked and within the grid.
        while head_pos in forbidden_coor or self.check_out_of_bounds(head_pos):
            head_pos = self.generate_loc()
        
        
        start_snake = [head_pos]
        forbidden_coor.append(head_pos)

        
        # Add tail to the back of the snake randomly to the desired length.
        for i in range(start_len):
            rand_dir = self.generate_rand_dir()
            prev = start_snake[i]
            temp = (prev[0]+rand_dir[0], prev[1] + rand_dir[1])
            while temp in forbidden_coor or self.check_out_of_bounds(temp):
                rand_dir = self.generate_rand_dir()
                temp = (prev[0]+rand_dir[0], prev[1] + rand_dir[1])
            start_snake.append(temp)
            forbidden_coor.append(temp)
        return start_snake


    def update_snake(self):
        oldHead = self.snake[0]
        newHead = (oldHead[0]+self.direction[0], oldHead[1]+self.direction[1]) 
        
        if self.check_out_of_bounds(newHead):
            self.game_over()
            return

        # Update food position  and add new part to snake if successfully eaten it.
        if newHead == self.food_pos:
            self.curr_score += 1
            increment = 5
            # increase the speed
            if self.speed > increment:  
                self.speed -= increment

            # add end to the tail
            new_tail = self.snake[-1]
            self.snake.append(new_tail)

            # generate food position not in snake or previous food pos.
            new_pos = self.generate_loc()
            while new_pos == self.food_pos or new_pos in self.snake:
                new_pos = self.generate_loc()

            self.food_pos = new_pos
            
            
        # remove the end of the snake for movement.
        self.snake.pop()
        

        if newHead in self.snake[1:]:
            self.game_over()
            return

        # Add another piece to the head since tail was removed.
        self.snake.insert(0, newHead)

if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()