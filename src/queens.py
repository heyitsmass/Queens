import ctypes 
from ctypes import cdll

lib = cdll.LoadLibrary('./src/libqueens.so')
#g++ -std=c++17 -fPIC -shared -o libqueens.so queens.cpp

lib.new_board.argtypes = [ctypes.c_int, ctypes.c_int, ctypes.c_int]
lib.new_board.restype = ctypes.POINTER(ctypes.c_char_p)
lib.display_board.argtypes = [ctypes.POINTER(ctypes.c_char_p)]
lib.display_board.restype = None 
lib.fen_formatter.argtypes = [ctypes.POINTER(ctypes.c_char_p)]
lib.fen_formatter.restype = ctypes.c_char_p

class Board(object): 
  def __init__(self, x, y, size=8): 
    self.obj = lib.new_board(x, y, size)
    self.fen = lib.fen_formatter(self.obj).decode('UTF-8')
    
  def display(self): 
    lib.display_board(self.obj) 

  def scan(self, x, y, size=8): 
    self.__del__() 
    self.obj = lib.new_board(x, y, size) 
    self.fen = lib.fen_formatter(self.obj).decode('UTF-8') 

  def __del__(self): 
    del self.obj
    del self.fen 
