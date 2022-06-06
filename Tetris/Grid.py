class TetrisGrid:
    def __init__(self, X, Y):
        self.X = X
        self.Y = Y
        self.grid = [self.get_clear_row() for j in range(self.Y)]
    
    def __str__(self):
        grid = ""
        for row in self.grid:
            grid += str(row)+"\n"
        return grid

    def calculate_score(self, rows):
        contiguous = 1
        r_len = len(rows)
        for i in range(r_len - 1):
            if rows[i+1] - rows[i] == 1:
                contiguous += 1
        rmdr = (r_len - contiguous) * 40

        if contiguous == 2:
            return 100 + rmdr 
        elif contiguous == 3:
            return 300 + rmdr
        elif contiguous == 4:
            return 1200 + rmdr
        else:
            return len(rows)* 40

    def check_if_space_left(self, x, y):
        if (x - 1) < 0:
            return True
        
        return self.grid[y][x - 1][0]

    def check_if_space_right(self, x, y):
        if (x + 1) >= self.X:
            return True
    
        return self.grid[y][x + 1][0]
    
    def check_if_space_underneath(self, x, y):
        if y + 1 >= self.Y:
            return True
        else:
            return self.grid[y + 1][x][0]

    def clear_full_rows(self):
        full_rows = self.get_full_indexes()
        score = self.calculate_score(full_rows)

        for row in full_rows:
            self.remove_row(row)
            self.replace_row()
        
        return score

    def fill_row(self, index):
        self.grid[index] = self.get_full_row()

    def get_full_indexes(self):
        full_indexes = []
        for y in range(self.Y):
            complete = True
            for x in range(self.X):
                if self.grid[y][x][0] == False:
                    complete = False
                    break
            if complete:
                full_indexes.append(y)
        
        return full_indexes
    
    def get_clear_row(self):
        return [(False, (0,0,0)) for i in range(self.X)]

    def get_draw_data(self):
        draw_data = []
        for y in range(self.Y):
            for x in range(self.X):
                if self.grid[y][x][0]:
                    draw_data.append((x,y, self.grid[y][x][1]))
        return draw_data

    def get_full_row(self):
        return [(True, (255,255,255)) for i in range(self.X)]

    def remove_row(self, index):
        self.grid.pop(index)
    
    def replace_row(self):
        self.grid.insert(0, self.get_clear_row())
    
    def update_loc(self, x, y, color):
        try:
            self.grid[y][x] = (True, color)
        except:
            print(x, y, "out of bounds")
        
