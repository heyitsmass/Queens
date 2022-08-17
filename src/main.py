"""
  Algorithm
  When looking at any row i:
    1. If row i contains the row of the initial queen (from the input), go to the next row
    2. Starting from column 0, and a column index j such that when the location for the queen at position
        [i, j] is safe
    3. Mark all the unsafe spots for the queen at position [i, j] and then go to row i + 1 and perform the
        same steps on this row, unless row i is the last row where in this case, the solution is found
    4. If no safe locations exist for a queen on row i, go back to row i - 1 and starting from the j column used
        in row i - 1. and the next safe location and then mark the board for the new unsafe locations and go
        to row i
"""

from dataclasses import dataclass
from copy import deepcopy 

@dataclass 
class Point: 
  x:int
  y:int
  queen:bool=False
  safe:bool=True  

  def __repr__(self): 
    if self.queen: 
      return " Q " 

    if not self.safe: 
      return " X " 

    return " * "

  def real(self): 
    return f"({self.x}, {self.y})"

class Board: 
  def __init__(self, size:int, x:int, y:int): 
    self.size = size 

    self.board = list()  

    for i in range(self.size): 
      row = list()
      for j in range(self.size): 
        row.append(Point(i, j))    
      self.board.append(row)

    self.queen = Point(x, y, True)  

    self.setQueen(x, y) 

    if not self.scan(self.board): 
      print("No Solution")  
    
    self.display() 

  def scan(self, board:list[list[Point]], i=0, j=0): 
    
    if i == self.queen.x: return self.scan(board, i+1) 
    if i >= self.size: return True 

    if board[i][j].safe: 
      old = deepcopy(board) 
      self.setQueen(i, j) 

      if self.scan(self.board, i+1): 
        return True; 
      
      self.board = old 
    
    if j+1 < self.size: 
      return self.scan(self.board, i, j+1) 
    
    return False; 


  def display(self): 
    for i in range(self.size): 
      print('  ' if not i else '', f'{i} ', end=' ')
    print() 
    for i, row in enumerate(self.board):
      for j, point in enumerate(row): 
        print(i if not j else '', point, end='') 
      print()  


  def setQueen(self, x:int, y:int): 
    if self.board[x][y].queen or not self.board[x][y].safe: 
      return False 
    self.board[x][y].queen = True 
    return self.setUnsafe(x, y)  
  
  def setUnsafe(self, x:int, y:int): 

    tmp_y = y - x 
    tmp_x = x + y 

    for i in range(self.size):
      self.board[x][i].safe = False
      self.board[i][y].safe = False

      if tmp_y + i in range(self.size):       
        self.board[i][tmp_y+i].safe = False

      if tmp_x - i in range(self.size):  
        self.board[tmp_x-i][i].safe = False

    return True 











