#include <iostream> 
#include <vector>  

using namespace std;

struct Point{ 
  public:  
    int x, y; 
    bool is_queen, is_safe;
    Point(int x, int y, bool is_queen=false, bool is_safe=true): x(x), y(y), is_queen(is_queen), is_safe(is_safe){}; 
    Point(){}; 
    std::string str() const{ 
      if(is_queen) return " Q "; 
      if(!is_safe) return " X "; 
      return " * "; 
    }
};

class Board{  
  public: 

    Board(int x, int y, int size=8){ 
      if(1 > x && y and x && y >= size+1)
        throw exception();  
      
      --x;      //normalize x
      --y;      //normalize y 

      this -> size = size; 
      
      /* Initialize the board */ 
      for(int i = 0; i < this->size; ++i){ 
        vector<Point> row; 
        for(int j = 0; j < this->size; ++j) 
          row.push_back(Point(i, j)); 
        chessboard.push_back(row);  
      } 

      /* create the source queen */ 
      source_queen = Point(x, y, true, false); 

      /* set the queen on the board */ 
      setQueen(x, y); 

      /* perform the scan */ 
      if(!scan(chessboard))
        cout << "No Solution (x=" << x << ", y=" << y << ')' << endl; 
      else
        cout << "Solution for point (x=" << x << ", y=" << y << ')' << endl; 
        display(); 
    }

    bool scan(vector<vector<Point> > const& board, int i=0, int j=0){ 
      if(i==source_queen.x) return scan(board, i+1);                    //skip the queen row
      if(i>=size) return true;                                          //if i >= size then a queen has been placed on every row


      if(board[i][j].is_safe){                                          //verify the space is free
        auto old = board;                                               //store a copy of the current board 
        setQueen(i, j);                                                 //attempt a queen set

        if(scan(chessboard, i+1))                                       //recursively check the next line until a return condition is met
          return true;                                                  //return true if the check succeeded

        chessboard = old;                                               //reset the board to the board prior to queen set and continue 
  
      }

      if(j+1<size)  
        return scan(chessboard, i, j+1);                                //check the next point in the row 
      
      return false;                                                     //if we cannot find a free space in the row, return false 
    } 


    void display(){ 
      for(int i = 0; i < size; ++i)                                     //output numbers for top row
        cout << ((!i)? "   " : "  ") << i+1 << " "; 
      cout << endl; 
      
      for(int i = 0; i < size; ++i){
        for(int j = 0; j < size; ++j){ 
          if(!j) cout << i+1 << ' '; 
          cout << chessboard[i][j].str() << ' '; 
        }
        cout << endl; 
      }
    }

    void setQueen(int x, int y){ 
      
      chessboard[x][y].is_queen = true;  

      /* Mark unsafe locations for the queen */ 

      int tl = y-x;         //top left 
      int tr = x+y;         //top right 

      for(int i = 0; i < size; ++i){ 
        chessboard[x][i].is_safe = false;       //left to right 
        chessboard[i][y].is_safe = false;       //top to bottom
        
        if(0 <= tr-i && tr-i < size)            //top right to bottom left
          chessboard[tr-i][i].is_safe = false; 

        if(0 <= tl+i && tl+i < size)            //top left to bottom right 
          chessboard[i][tl+i].is_safe = false; 
      }
    }

    int size;       
    std::vector<std::vector<Point> > chessboard; 
    Point source_queen; 
};

int main(int argv, char** argc){  

  /* Output the solution (if available) for every position */ 

  for(int i = 1; i < 9; i++){ 
    for(int j = 1; j < 9; j++){ 
      Board(i, j);  
    }
  }
 
  return 0; 
} 
