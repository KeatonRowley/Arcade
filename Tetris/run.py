from enum import Enum, unique
import pygame
from pygame.locals import *
import math
import random
import Shapes
import Grid

# Image resources.
background_img_name = ".\Images\GrassBackground.jpg"

# Sound resources
MUSIC_TRACK = ".\Sounds\The-Underscore-Orkestra-Hungarian-Dance-The-Underscore-Orkestra.wav"
SCORE_1_SOUND = ".\Sounds\Score1Sound.wav"
SCORE_2_SOUND = ".\Sounds\Score2Sound.wav"
SCORE_3_SOUND = ".\Sounds\Score3Sound.wav"
SCORE_4_SOUND = ".\Sounds\Score4Sound.wav"
SHAPE_LAND_SOUND = ".\Sounds\ShapeLandSound.wav"


# Shape indexes.
LChiralL = 1
LChiralR = 2
Line = 3
SChiralL = 4
SChrialR = 5
Square = 6
T = 7

# color resources
WHITE = (255,255,255)
BLACK = (0, 0, 0)
RED = (255, 0, 0)

IN_PLAY = 0
GAME_OVER = 1
STARTING_GAME = 2




class App:
    def __init__(self):
        self.speed_down = False
        self.speed_right = False
        self.speed_left = False
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.blockSize = 20 # size of the grid
        self.board_size = self.gridWidth, self.gridHeight = 20, 32
        self.clock = pygame.time.Clock()
        self.size = self.width, self.height = self.gridWidth*self.blockSize, self.gridHeight*self.blockSize
        self.grid = Grid.TetrisGrid(self.gridWidth, self.gridHeight)
        self.curr_shape = [BLACK, (0,0), Shapes.Square]
        self.score = 0
        self.time_left= 0
        self.time_right = 0
        self.time_down = 0
        self.delay = True

        self.piece_set = True

    
    def on_init(self):
        pygame.init()
        pygame.mixer.music.load(MUSIC_TRACK)
        self.score_1_sound = pygame.mixer.Sound(SCORE_1_SOUND)
        self.score_2_sound = pygame.mixer.Sound(SCORE_2_SOUND)
        self.score_3_sound = pygame.mixer.Sound(SCORE_3_SOUND)
        self.score_4_sound = pygame.mixer.Sound(SCORE_4_SOUND)
        self.shape_land_sound = pygame.mixer.Sound(SHAPE_LAND_SOUND)
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF, pygame.HWSURFACE)
        self._running = True
        self.game_state = STARTING_GAME
        self.speed = 800 # number of milliseconds between updates.
        self.load_background()
        self.time_elapsed_since_last_action = 0
    

    # Calls proper 
    def on_event(self, event):
        if event.type == QUIT:
            self.on_exit()

        elif event.type == pygame.KEYDOWN:
    
            if self.game_state == STARTING_GAME:
                if event.key == pygame.K_SPACE:
                    self.game_state = IN_PLAY
                    
                    pygame.mixer.music.play(-1)
                    self.reset_game()

            if self.game_state == GAME_OVER:
                if event.key == pygame.K_SPACE:
                    self.game_state = IN_PLAY
                    sound = pygame.mixer.Sound(MUSIC_TRACK)
                    pygame.mixer.music.play(-1)
           
            if self.game_state == IN_PLAY:
                if event.key == pygame.K_LEFT:
                    if self.check_left() == False:
                        self.curr_shape.update_left()
                        self.turn_on_left_speed()

                elif event.key == pygame.K_RIGHT:
                    if self.check_right() == False:
                        self.curr_shape.update_right()
                        self.turn_on_right_speed()

                elif event.key == pygame.K_DOWN:
                    self.speed_down = True
                    
                elif event.key == pygame.K_w:
                    self.curr_shape.rotate_ccw()

                elif event.key == pygame.K_e:
                    self.curr_shape.rotate_cw()

        elif self.game_state == IN_PLAY:
            if self.piece_set == True:
                self.generate_new_piece()
                self.piece_set = False
        
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_DOWN:
                self.turn_off_down_speed()
            
            elif event.key == pygame.K_RIGHT:
                self.turn_off_right_speed()

            elif event.key == pygame.K_LEFT:
                self.turn_off_left_speed()
     
    def on_loop(self):
        self.load_background()

        if self.game_state == STARTING_GAME:
            self.print_text("PRESS SPACE TO START GAME")
            pass
        
        elif self.game_state == IN_PLAY:
            self.check_game()
            self.draw_shape()
            self.draw_pieces()
            self.draw_grid()
        
        elif self.game_state == GAME_OVER:
            self.print_text("GAME OVER PRESS SPACE TO START GAME", font_size = 15)
            pass
        
        self.print_text("Score: " + str(self.score), x = self.width // 10 * 8, y = self.height // 20 * 1 + 5)

    def on_render(self):
        self._display_surf.blit(self._image_surf, (0,0))
        pygame.display.flip()

    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        if self.on_init() == False:
            self._running = False
 
        while(self._running):
            for event in pygame.event.get():
                self.on_event(event)
            
            self.on_loop()
            self.on_render()
        self.on_cleanup()
    
    def on_exit(self):
        self._running = False
 
    def draw_grid(self):
        for x in range(0, self.width, self.blockSize):
            for y in range(0, self.height, self.blockSize):
                self.draw_box((x, y), WHITE, 1, 1)               
    
    def draw_box(self, pos, color, mult, offset = 0):
        x, y = pos
        rect = pygame.Rect(x*mult, y*mult, self.blockSize, self.blockSize)
        pygame.draw.rect(self._image_surf, color, rect, offset)
    
    def draw_shape(self):
        locs, color = self.curr_shape.get_shape_data()
        for loc in locs:
            self.draw_box(loc, color, self.blockSize)

    def draw_pieces(self):
        data = self.grid.get_draw_data()
        for d in data:
            row, col, color = d[0],d[1],d[2]
            self.draw_box((row,col), color, self.blockSize)


    def get_random_choice(self, bottom, top):
        return random.randint(bottom, top)


    def generate_new_piece(self):
        self.reset_speed()
        
        shape_choice = self.get_random_choice(1,7)

        if shape_choice == LChiralL:
            self.curr_shape = Shapes.LChiralL(self.board_size)
        elif shape_choice == LChiralR:
            self.curr_shape = Shapes.LChiralR(self.board_size)
        elif shape_choice == Line:
            self.curr_shape = Shapes.Line(self.board_size)
        elif shape_choice == SChiralL:
            self.curr_shape = Shapes.SChiralL(self.board_size)
        elif shape_choice == SChrialR:
            self.curr_shape = Shapes.SChiralR(self.board_size)
        elif shape_choice == Square:
            self.curr_shape = Shapes.Square(self.board_size)
        elif shape_choice == T:
            self.curr_shape = Shapes.T(self.board_size)
        

        

       
    def check_game(self):

        dt = self.clock.tick()

        if self.speed_right:
            self.time_right += dt
            for i in range(int(self.time_right / 2000)):
                    if self.check_right() == False:
                        self.curr_shape.update_right()

        if self.speed_left:
            self.time_left += dt
            for i in range(int(self.time_left / 2000)):
                    if self.check_left() == False:
                        self.curr_shape.update_left()
        
        if self.speed_down:
            self.speed_down += dt
            for i in range(int(self.speed_down / 2000)):
                self.update_game()


        self.time_elapsed_since_last_action += dt

        if self.time_elapsed_since_last_action >= self.speed:
            self.time_elapsed_since_last_action = 0
            self.update_game()

    def check_left(self):
        locs, color = self.curr_shape.get_shape_data()
        for loc in locs:
            if self.grid.check_if_space_left(loc[0],loc[1]):
                return True
        return False
    
    def check_right(self):
        locs, color = self.curr_shape.get_shape_data()
        for loc in locs:
            if self.grid.check_if_space_right(loc[0],loc[1]):
                return True
        return False
    
    def check_shape_lock(self):
        locs, color = self.curr_shape.get_shape_data()
        for loc in locs:
            if self.grid.check_if_space_underneath(loc[0],loc[1]):
                return True

    def load_background(self):
        # Load background image
        self._image_surf = pygame.image.load(background_img_name).convert()
        self._image_surf = pygame.transform.scale(self._image_surf, (1280, 720))
        return False

    def lock_piece(self):
        pygame.mixer.Sound.play(self.shape_land_sound)
        locs, color = self.curr_shape.get_shape_data()
        game_over = 0
        for loc in locs:
            self.grid.update_loc(loc[0], loc[1], color)

            if loc[1] <= 0:
                self.game_state = GAME_OVER
                pygame.mixer.music.stop()
                self.reset_game()
                return
        if self.speed > 5:
            self.speed -= 5
    
    def print_text(self, message = "", x = None, y = None, font_size = 20):
        if x is None:
            x = self.width // 2
        if y is None:
            y = self.height // 2
        pygame.font.init()
        font = pygame.font.SysFont('Comic Sans MS', font_size)
        text = font.render(message, True, RED)
        text_rect = text.get_rect()
        text_rect.center = (x, y)
        self._image_surf.blit(text, text_rect)
    
    def reset_game(self):
        self.grid = Grid.TetrisGrid(self.gridWidth, self.gridHeight)
        self.curr_shape = self.generate_new_piece()
        self.score = 0
        self.reset_speed()
        self.delay = True
        self.speed = 800
    
    def reset_speed(self):
        self.turn_off_down_speed()
        self.turn_off_left_speed()
        self.turn_off_right_speed()
       
    def turn_on_left_speed(self):
        self.speed_left = True
        self.time_left = 0

    def turn_on_right_speed(self):
        self.speed_right = True
        self.time_right = 0
    
    def turn_on_down_speed(self):
        self.speed_down = True
        self.time_down = 0
    
    def turn_off_left_speed(self):
        self.speed_left = False
        self.time_left = 0

    def turn_off_right_speed(self):
        self.speed_right = False
        self.time_right = 0
    
    def turn_off_down_speed(self):
        self.speed_down = False
        self.time_down = 0
    
    def update_board(self):
        score = self.grid.clear_full_rows()
        self.update_score(score)
        

    def update_game(self):
        if self.check_shape_lock():
            if self.delay == True:
                self.delay = False
                return
            self.lock_piece()
            self.generate_new_piece()
            self.update_board()
            self.delay == True
        self.curr_shape.update_down()
    
    def update_score(self, score):
        self.score += score
        if score == 40:
            pygame.mixer.Sound.play(self.score_1_sound)
        elif score == 100:
            pygame.mixer.Sound.play(self.score_2_sound)
        elif score == 300:
            pygame.mixer.Sound.play(self.score_3_sound)
        elif score == 1200:
            pygame.mixer.Sound.play(self.score_4_sound)


if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()