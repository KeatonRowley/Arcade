from abc import ABC, abstractmethod
import math
import numpy as np
import random

I3 = np.array(
    [[1,0,0],
    [0,1,0],
    [0,0,1]]
)

I4 = np.array(
    [[1,0,0,0],
    [0,1,0,0],
    [0,0,1,0],
    [0,0,0,1]]
)

IMH3 = np.array(
    [[0,0,1],
    [0,1,0],
    [1,0,0]]
)

IMH4 = np.array(
    [[0,0,0,1],
    [0,0,1,0],
    [0,1,0,0],
    [1,0,0,0]]
)


RED = 1
ORANGE = 2
YELLOW = 3
GREEN = 4
BLUE = 5
PURPLE = 6
NONE = 7

colorIdx =  {
    RED: (255, 0, 0),
    ORANGE : (255, 127, 0),
    YELLOW : (255, 255, 0),
    GREEN : (0, 255, 0),
    BLUE : (0, 0, 255),
    PURPLE : (255, 0, 255),
    NONE : (0, 0, 0)
}



class Shape:
    def __init__(self, max_x, max_y):
        self.rotate_bit = True
        self.max_X = max_x
        self.max_Y = max_y
        self.X = self.generate_x_pos(self.max_X)
        self.Y = -2
        self.Color = self.generate_color()
        self.generate_orientation()
        
    
    def check_tup_range(self, t):
        return (t[0] >= 0 
        and t[0] < self.max_X 
        and t[1] >= 0
        and t[1] < self.max_Y)

    def rotate_cw(self):
        self.grid = np.dot(np.transpose(self.grid), IMH3)
        if len(self.calculate_fill_grid()) < 4 and self.rotate_bit:
            self.rotate_bit = False
            self.rotate_ccw()
        self.rotate_bit = True

    def rotate_ccw(self):
        self.grid = np.dot(IMH3, np.transpose(self.grid))
        if len(self.calculate_fill_grid()) < 4 and self.rotate_bit:
            self.rotate_bit = False
            self.rotate_cw()
        self.rotate_bit = True

    def update_left(self):
        self.X -= 1
        if len(self.calculate_fill_grid()) < 4:
            self.X += 1
            return 

    def update_right(self):
        self.X += 1
        if len(self.calculate_fill_grid()) < 4:
            self.X -= 1
            return 
        
    
    def update_down(self):
        if self.Y < self.max_Y:
            self.Y += 1
    
    def generate_color(self):
        color_choice = random.randint(1, 6)
        return colorIdx[color_choice]

    def generate_x_pos(self, max):
        return random.randint(2,(max-2))
    
    def generate_orientation(self):
        orientation = random.randint(0, 3)
        for i in range(orientation):
            self.rotate_cw()

    def calculate_fill_grid(self):
        mxl = self.X 
        myl = self.Y

        x0 = mxl-1
        x1 = mxl
        x2 = mxl+1

        y0 = myl-1
        y1 = myl
        y2 = myl+1
        

        small_grid = [
            (x0,y0),(x0,y1),(x0,y2),
            (x1,y0),(x1,y1),(x1,y2),
            (x2,y0),(x2,y1),(x2,y2),
        ]

        true_pos = np.nonzero(self.grid.flatten())[0]
        coord = [small_grid[pos] for pos in true_pos if self.check_tup_range(small_grid[pos])] 
        return coord

    def get_shape_data(self):
        return self.calculate_fill_grid(), self.Color

    def __str__(self):
        return str((self.X, self.Y)) +"\n" + str(self.grid) + "\n"+ str(self.Color) +"\n"


class LChiralL(Shape):
    def __init__(self, boundry):
        self.grid = np.array(
            [[1,1,0],
            [0,1,0],
            [0,1,0]]
        )
        super().__init__(boundry[0], boundry[1])

class LChiralR(Shape):
    def __init__(self, boundry):
        self.grid = np.array(
                [[0,1,1],
                [0,1,0],
                [0,1,0]]
            )
        super().__init__(boundry[0], boundry[1])
        
    
class Line(Shape):
    def __init__(self, boundry):
        self.rotate_bit = True
        self.max_X = boundry[0]
        self.max_Y = boundry[1]
        self.X = self.generate_x_pos(self.max_X)
        self.Y = -2
        self.Color = self.generate_color()
        
        self.grid = np.array(
                [[0,1,0,0],
                [0,1,0,0],
                [0,1,0,0],
                [0,1,0,0]]
            )

        self.generate_orientation()
        
    
    def rotate_cw(self):
        self.grid = np.dot(np.transpose(self.grid), IMH4)
        
        # If the change is outside the grid, undo it.
        if len(self.calculate_fill_grid()) < 4 and self.rotate_bit:
            self.rotate_bit = False
            self.rotate_ccw()
    
        self.rotate_bit = True

    def rotate_ccw(self):
        self.grid = np.dot(IMH4, np.transpose(self.grid))
        # If the change is outside the grid, undo it.
        if len(self.calculate_fill_grid()) < 4 and self.rotate_bit:
            self.rotate_bit = False
            self.rotate_cw()
        
        self.rotate_bit = True

    def calculate_fill_grid(self):
        mxl = int(math.floor(self.X + 0.5))
        myl = int(math.floor(self.Y + 0.5))

        x0 = mxl-1
        x1 = mxl
        x2 = mxl+1
        x3 = mxl+2

        y0 = myl-1
        y1 = myl
        y2 = myl+1
        y3 = myl+2

        small_grid = [
            (x0,y0),(x0,y1),(x0,y2),(x0,y3),
            (x1,y0),(x1,y1),(x1,y2),(x1,y3),
            (x2,y0),(x2,y1),(x2,y2),(x2,y3),
            (x3,y0),(x3,y1),(x3,y2),(x3,y3),
        ]

        true_pos = np.nonzero(self.grid.flatten())[0]
        coord = [small_grid[pos] for pos in true_pos if self.check_tup_range(small_grid[pos])] 
        return coord
    
class SChiralL(Shape):
    def __init__(self, boundry):
        self.grid = np.array(
                [[0,1,0],
                [1,1,0],
                [1,0,0]]
            )
        super().__init__(boundry[0], boundry[1])
        
class SChiralR(Shape):
    def __init__(self, boundry):
        
        self.grid = np.array(
                [[0,1,0],
                [0,1,1],
                [0,0,1]]
            )
        super().__init__(boundry[0], boundry[1])
        
        

class Square(Shape):
    def __init__(self, boundry):
        self.grid = np.array(
                [[1,1],
                [1,1]]
            )
        super().__init__(boundry[0], boundry[1])
    
    def calculate_fill_grid(self):
        mxl = self.X
        myl = self.Y

        small_grid = [
            (mxl,myl),(mxl,myl+1),
            (mxl+1,myl),(mxl+1,myl+1) 
        ]

        true_pos = np.nonzero(self.grid.flatten())[0]
        coord = [small_grid[pos] for pos in true_pos if self.check_tup_range(small_grid[pos])] 
        return coord
       
    def rotate_cw(self):
        pass
    def rotate_ccw(self):
        pass
    
class T(Shape):
    def __init__(self, boundry):
        self.grid = np.array(
                [[0,1,0],
                [1,1,1],
                [0,0,0]]
            )

        super().__init__(boundry[0], boundry[1])
        
        
        
        
