#include <iostream> 
#include <vector> 

using namespace std; 

struct Point{ 
  public:  
    int x, y; 
    bool queen, safe;
    Point(int i, int j, bool q = false, bool s = true): x(i), y(j), queen(q), safe(s) {};
    Point(): x(0), y(0), queen(false), safe(true) {}; 
    std::string repr() const{ 
      if(queen) return " Q "; 
      if(!safe) return " X "; 
      return " * "; 
    }
};

class Board{ 

  int size; 
  vector<vector<Point> > board;  
  Point queen; 
  public: 
    Board(int x, int y, int s=8){
      size = s; 
      
      for(int i = 0; i < size; i++){ 
        vector<Point> row; 
        for(int j = 0; j < size; j++){ 
          row.push_back(Point(i, j)); 
        }
        board.push_back(row); 
      }

      queen = Point(x, y, true);  
      setQueen(x, y); 

      if(scan(board)) 
        display(); 
      else 
        cout << "No Solution" << endl; 
      
    } 
    bool scan(vector<vector<Point> > inp_board, int i=0, int j=0){ 
      
      if(i==queen.x) return scan(inp_board, i+1); 
      if(i>=size) return true;

      if(inp_board[i][j].safe){
        auto old = inp_board;  
        setQueen(i, j);           //set queen sets a queen on the board contained within the class

        if(scan(board, i+1))      //we pass the class's board  instead of inp_board for that reason 
          return true; 
        
        board = old;              //then reset the board 
      }

      if(j+1<size)
        return scan(board, i, j+1);
       
      return false; 
    }
    bool setQueen(int x, int y){ 
      if (board[x][y].queen || !board[x][y].safe)
        return false;  
      board[x][y].queen = true; 
      return setUnsafe(x, y);  
    }
    bool setUnsafe(int x, int y){ 
      int tmp_y = y-x; 
      int tmp_x = x+y; 

      for(int i = 0; i < size; i++){ 
        board[x][i].safe = false; 
        board[i][y].safe = false; 

        if(tmp_y+i >= 0 && tmp_y+i < 8)
          board[i][tmp_y+i].safe = false; 
        
        if(tmp_x-i >= 0 && tmp_x-i < 8)
          board[tmp_x-i][i].safe = false; 

      }
      return true; 
    }

    void display(){ 
      for(int i = 0; i < size; i++)
        cout << ((i > 0)? "  " : "   ") << i << " ";
      cout << endl; 
      for(int i =0; i < size; i++){ 
        for(int j =0; j < size; j++){ 
          if(!j) cout << i << " "; 
          cout << board[i][j].repr() << ' '; 
        }
        cout << endl; 
      }
    }
}; 

int main(int argv, char** argc){ 

  Board chessboard(0, 0); 

  return 0; 
}