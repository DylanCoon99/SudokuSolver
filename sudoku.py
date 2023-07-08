import math as m
'''
Sudoku solver via backtracking
by Dylan Coon

Backtracking Algoritm - 

    (1) Assign numbers to empty cells one by one
        - before assigning, check to make sure it is valid (not already in row, column, or subgrid)
    
    (2) Recursively check whether this assignment doesn't lead to a solution
    
    (3) Try the next number for the current empty cell
    
    (4) If no number (1 - 9) leads to a solution --> return false (No solution exists)
    
    subgrids:

        [1] [2] [3]
        [4] [5] [6]
        [7] [8] [9]

'''



def print_grid(grid):
    # prints the sudoku grid
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end = " ")
        print()


def solve_sudoku(grid):

    return

def is_safe(grid, row, col, num):
    # determine whether or not a number can go in a particular location
    
    # calculate subgrid_num
    subgrid_num = subgrid_map[(m.ceil((row + 1) / 3) , m.ceil((col + 1) / 3))]
    
    # check if row, col, and subgrid is safe
    return not (in_row(grid, row, num) or in_col(grid, col, num) or in_subgrid(grid, subgrid_num, num))


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
def in_subgrid(grid, subgrid_num, num):
    # remember: frequency is zero indexed
    if(frequency_map[subgrid_num - 1][num] == 1):
        return True
    return False

if __name__=="__main__":
    # Define the size of the grid
    N = 9

    # creating a 2D array for the grid
    grid =[[0 for x in range(N)]for y in range(N)]
     
    # assigning values to the grid
    grid =[[3, 0, 6, 5, 0, 8, 4, 0, 0],
          [5, 2, 0, 0, 0, 0, 0, 0, 0],
          [0, 8, 7, 0, 0, 0, 0, 3, 1],
          [0, 0, 3, 0, 1, 0, 0, 8, 0],
          [9, 0, 0, 8, 6, 3, 0, 0, 5],
          [0, 5, 0, 0, 9, 0, 6, 0, 0],
          [1, 3, 0, 0, 0, 0, 2, 5, 0],
          [0, 0, 0, 0, 0, 0, 0, 7, 4],
          [0, 0, 5, 2, 0, 6, 3, 0, 0]]
    

    # make a list of dictionaries that indicate the frequency of each number in each subgrid
    d = dict()
    for i in range(1,N + 1):
        d[str(i)] = 0
    frequency_map = [d for i in range(1,N + 1)]

    subgrid_map = {(1, 1): 1, (1, 2): 2, (1, 3): 3,
                   (2, 1): 4, (2, 2): 5, (2, 3): 6, 
                   (3, 1): 7, (3, 2): 8, (3, 3): 9}

    # if success print the grid
    if(solve_sudoku(grid)):
        print_grid(grid)
    else:
        print ("No solution exists")