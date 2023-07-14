def check_validity(board, x, y, num):
    grid_x = (x // 3) + 1
    grid_y = (y // 3) + 1
    grid = [columns[(grid_y - 1) * 3: grid_y * 3] for columns in board[(grid_x - 1) * 3: grid_x * 3]]
    if any(str(num) == c for c in board[x]): return False
    if any(str(num) == k for k in [c[y] for c in board]): return False
    if any(str(num) in c for c in grid): return False
    return True


sudoku = [
    ['5', '.', '.', '6', '.', '.', '.', '.', '.'],
    ['8', '.', '.', '.', '.', '.', '.', '9', '.'],
    ['.', '3', '.', '.', '5', '2', '.', '.', '4'],
    ['.', '.', '.', '7', '.', '.', '.', '.', '1'],
    ['3', '.', '.', '.', '6', '1', '8', '.', '.'],
    ['.', '6', '.', '4', '.', '.', '.', '.', '.'],
    ['.', '5', '.', '.', '1', '3', '.', '.', '2'],
    ['.', '.', '.', '.', '.', '7', '.', '.', '.'],
    ['.', '.', '2', '.', '.', '.', '4', '.', '.']
]

def sudoku_backtracker(x = 0, y = 0, value = 1):
    if sudoku[x][y] != '.' and y < 8: 
        sudoku_backtracker(x, y + 1, 1)
        return
    elif sudoku[x][y] != '.' and y == 8 and x < 8: 
        sudoku_backtracker(x + 1, 0, 1)
        return
    elif sudoku[x][y] != '.' and y == 8 and x == 8:
        print(sudoku)
        return
    
    if check_validity(sudoku, x, y, value) and y < 8:
        sudoku[x][y] = str(value)
        sudoku_backtracker(x, y + 1, 1)
        sudoku[x][y] = '.'

    elif check_validity(sudoku, x, y, value) and y == 8 and x < 8:
        sudoku[x][y] = str(value)
        sudoku_backtracker(x + 1, 0, 1)
        sudoku[x][y] = '.'
    
    elif check_validity(sudoku, x, y, value) and y == 8 and x == 8:
        sudoku[x][y] = str(value)
        print(sudoku)
        return
    
    if value == 9:
        return
    
    sudoku_backtracker(x, y, value + 1)


sudoku_backtracker()



