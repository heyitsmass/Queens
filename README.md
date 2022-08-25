# Eight-Queens

Produces a *valid* FEN sequence for a chessboard of nxn size with n number of queens such that no queen is attacking another. 

> The FEN sequence (Forsyth–Edwards Notation) is *valid* because it does not hold color, king, en pessant, castling, or score rules. Simply placements of queens.
> Similarly, the fen increases in length depending on board size 


### Notes: 

- The x and y values of the initial queen are bound to the size of the board; both must be within range (0, size]  
- The size of the board should be within range (2, 25]; Any size greater than 25 will incur performance penalties.
- Size defaults to 8


### Usage: 
```python3
import queens 

# initialize a new board of size 8 with an initial queen (3, 4)
chessboard = queens.Board(3, 4) 

chessboard.display() 

'''Output: 

     1   2   3   4   5   6   7   8 
  1  Q   X   X   X   X   X   X   X  
  2  X   X   X   X   X   X   Q   X  
  3  X   X   X   Q   X   X   X   X  
  4  X   X   X   X   X   Q   X   X  
  5  X   X   X   X   X   X   X   Q  
  6  X   Q   X   X   X   X   X   X  
  7  X   X   X   X   Q   X   X   X  
  8  X   X   Q   X   X   X   X   X  
  
'''

print(chessboard.fen) 

#>>> Q7/6Q1/3Q4/5Q2/7Q/1Q6/4Q3/2Q5

chessboard.scan(2, 3, size=15) 

chessboard.display() 

'''Output: 

    1   2   3   4   5   6   7   8   9  10  11  12  13  14  15 
1   Q   X   X   X   X   X   X   X   X   X   X   X   X   X   X  
2   X   X   Q   X   X   X   X   X   X   X   X   X   X   X   X  
3   X   X   X   X   Q   X   X   X   X   X   X   X   X   X   X  
4   X   Q   X   X   X   X   X   X   X   X   X   X   X   X   X  
5   X   X   X   X   X   X   X   X   X   Q   X   X   X   X   X  
6   X   X   X   X   X   X   X   X   X   X   X   Q   X   X   X  
7   X   X   X   X   X   X   X   X   X   X   X   X   X   Q   X  
8   X   X   X   Q   X   X   X   X   X   X   X   X   X   X   X  
9   X   X   X   X   X   X   X   X   X   X   X   X   Q   X   X  
10  X   X   X   X   X   X   X   X   Q   X   X   X   X   X   X  
11  X   X   X   X   X   Q   X   X   X   X   X   X   X   X   X  
12  X   X   X   X   X   X   X   X   X   X   X   X   X   X   Q  
13  X   X   X   X   X   X   Q   X   X   X   X   X   X   X   X  
14  X   X   X   X   X   X   X   X   X   X   Q   X   X   X   X  
15  X   X   X   X   X   X   X   Q   X   X   X   X   X   X   X  

'''

print(chessboard.fen) 

#>>> Q14/2Q12/4Q10/1Q13/9Q5/11Q3/13Q1/3Q11/12Q2/8Q6/5Q9/14Q/6Q8/10Q4/7Q7
```

### Algorithm 
```cpp
bool Board::scan(std::vector<std::vector<Point> > const& b, int x, int y){ 
  if(x==queen.x) return scan(b, x+1);                    //skip the queen row
  if(x>=size) return true;                               //if i >= size then a queen has been placed on every row

  if(b[x][y].safe){                                      //verify the space is free
    auto o = b;                                          //store a copy of the current board 
    set(x, y);                                           //attempt a queen set

    if(scan(cb, x+1)){                                   //recursively check the next line until a return condition is met
      if(cb[x][y].queen && x < size)
        queens.push_back(cb[x][y]);
      return true;                                       //return true if the check succeeded
    }
    cb = o;                                              //reset the board to the board prior to queen set and continue 
  }

  if(y+1<size)  
    return scan(cb, x, y+1);                             //check the next point in the row 
  
  return false;    
}
```
