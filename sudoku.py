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
    for i in range(N):
        for j in range(N):
            print(grid[i][j], end = " ")
        print()


def solve_sudoku(grid):
    return

def is_safe(grid, row, col, num):
    # determine whether or not a number can go in a particular location
    current_row = grid[row]
    
    # check if row is safe

    
    # check if column is safe

    
    # check if subgrid is safe

    return

def in_subgrid(grid, subgrid_num, num):
    return

if __name__=="__main__":
    # Define the size of the grid
    N = 9

    # creating a 2D array for the grid
    grid =[[0 for x in range(9)]for y in range(9)]
     
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
     
    # if success print the grid
    if(solve_sudoku(grid)):
        print_grid(grid)
    else:
        print ("No solution exists")