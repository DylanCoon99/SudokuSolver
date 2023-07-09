import math as m
import config

N = 9

'''
Sudoku solver via backtracking
by Dylan Coon

Backtracking Algoritm - 

    (1) Assign numbers to empty cells one by one
        - before assigning, check to make sure it is valid (not already in row, column, or subgrid)
    
    (2) Recursively check whether this assignment doesn't lead to a solution
    
    (3) Try the next number for the current empty cell
    
    (4) If no number (1 - 9) leads to a solution --> return false (No solution exists)
    

'''



def print_grid(grid):
    # prints the sudoku grid
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end = " | ")
        print()


def solve_sudoku(grid):

    t = find_unassigned(grid)
    if t == None: return True

    row = t[0]
    col = t[1]

    # for any unassigned (=0) location
        # choose a number 1-9
        # check if that number is safe
        # if not safe 

    for i in range(1, N + 1):
        if is_safe(grid, row, col, i):
            
            # update the grid
            grid[row][col] = i

            if(solve_sudoku(grid)): return True

            # did not solve --> backtrack
            grid[row][col] = 0
            

    return False

    


def find_unassigned(grid):
    # finds the first instance of an unassigned element in the grid
    for i in range(N):
        for j in range(N):
            if grid[i][j] == 0:
                return (i, j)
    return None

def is_safe(grid, row, col, num):
    # determine whether or not a number can go in a particular location
    
    # calculate subgrid_num
    #subgrid_num = subgrid_map[(m.ceil((row + 1) / 3) , m.ceil((col + 1) / 3))]
    
    # check if row, col, and subgrid is safe
    return not (in_row(grid, row, num) or in_col(grid, col, num) or in_subgrid(grid, row - row % 3, col - col % 3, num))


# returns true if num in row, false otherwise 
def in_row(grid, row, num):
    current_row = grid[row]
    for e in current_row:
        if e == num:
            return True
    return False


# returns true if num in col, false otherwise
def in_col(grid, col, num):
    for r in grid:
        if r[col] == num:
            return True
    return False


# returns true if num in subgrid, false otherwise
def in_subgrid(grid, row, col, num):
    for i in range(N//3):
        for j in range(N//3):
            if(grid[i + row][j + col] == num):
                return True
    return False

if __name__=="__main__":

    N = 9

    # creating a 2D array for the grid
    grid =[[0 for x in range(N)]for y in range(N)]

    '''
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    '''

    # make a list of dictionaries that indicate the frequency of each number in each subgrid
    d = dict()
    for i in range(1,N + 1):
        d[str(i)] = 0
    frequency_map = [d for i in range(1,N + 1)]

    # generate the frequency map
    # ...
    #update_frequency_map(grid)

    #subgrid_map = {(1, 1): 1, (1, 2): 2, (1, 3): 3,
                   #(2, 1): 4, (2, 2): 5, (2, 3): 6, 
                   #(3, 1): 7, (3, 2): 8, (3, 3): 9}

    # if success print the grid
    if(solve_sudoku(grid)):
        print_grid(grid)
    else:
        print ("No solution exists")