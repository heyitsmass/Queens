from src import queens

board = queens.Board(1, 5)

board.display()

print(board.fen)

board.scan(2, 3) 

board.display()  

print(board.fen)
