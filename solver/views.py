from django.shortcuts import render
from django.http import HttpResponse
from .logic import solve_sudoku

def index(request):
    # Initialize an empty 9x9 board
    board = [[0 for _ in range(9)] for _ in range(9)]
    
    if request.method == 'POST':
        # Retrieve data from form
        try:
            for i in range(9):
                for j in range(9):
                    cell_value = request.POST.get(f'cell_{i}_{j}')
                    if cell_value and cell_value.isdigit():
                        board[i][j] = int(cell_value)
                    else:
                        board[i][j] = 0
            
            # Solve the board
            # We need a copy of the board to check if it's solveable easily or just pass it
            # solve_sudoku modifies in place
            
            solve_sudoku(board)
            
        except Exception as e:
            # Handle errors gracefully (maybe add an error message context)
            pass

    return render(request, 'solver/index.html', {
        'board': board,
        'range_9': range(9) # For template loop
    })
