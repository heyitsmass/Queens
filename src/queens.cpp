#include <iostream> 
#include "queens.h"


inline std::string to_string(bool v){return (v)? "True " : "False";}

Point::Point(int x, int y, bool queen=false, bool safe=true){ 
  this -> x = x; 
  this -> y = y; 
  this -> queen = queen; 
  this -> safe = safe; 
}

inline std::string Point::str() const{ 
  if(queen) return " Q "; 
  if(!safe) return " X "; 
  return " * "; 
}

inline std::string Point::raw() const{ 
  return "Point(x=" + std::to_string(x) + ", y=" + std::to_string(y) + ", queen=" + to_string(queen) + ", safe=" + to_string(safe) + ")";
}

Board::Board(int x, int y, int size=8){ 
  if(1 > x && y and x && y >= size+1)
    throw std::exception();  
  
  --x;      //normalize x
  --y;      //normalize y 

  this -> size = size; 
  
  /* Initialize the board */ 
  for(int i = 0; i < this->size; ++i){ 
    std::vector<Point> row; 
    for(int j = 0; j < this->size; ++j) 
      row.push_back(Point(i, j)); 
    cb.push_back(row);  
  } 

  /* create the source queen */ 
  queen = Point(x, y, true, false); 

  /* set the queen on the board */ 
  set(x, y);

  /* perform the scan */ 
  scan(cb); 

  /* emplace a queen */ 
  queens.emplace(queens.end()-queen.x, queen);

}

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

void Board::display(){ 
  for(int x = 0; x < size; ++x)                          //output numbers for top row
    std::cout << ((!x)? "   " : "  ") << x+1 << ' '; 
  std::cout << std::endl; 
  
  for(int x = 0; x < size; ++x){                         //output each point on the board 
    for(int y = 0; y < size; ++y){ 
      if(!y)std::cout << x+1 << ' ';
      std::cout << cb[x][y].str() << ' '; 
    }
    std::cout << std::endl; 
  }
}


void Board::set(int x, int y){ 
      
  cb[x][y].queen = true;  

  /* Mark unsafe locations for the queen */ 

  int tl = y-x;                                          //top left 
  int tr = x+y;                                          //top right 

  for(int i = 0; i < size; ++i){ 
    cb[x][i].safe = false;                               //left to right 
    cb[i][y].safe = false;                               //top to bottom
    
    if(0 <= tr-i && tr-i < size)                         //top right to bottom left
      cb[tr-i][i].safe = false; 

    if(0 <= tl+i && tl+i < size)                         //top left to bottom right 
      cb[i][tl+i].safe = false; 
  }
}

inline std::vector<std::vector<Point> > Board::getBoard() const{ 
  return cb; 
}

inline int Board::getSize() const noexcept{ 
  return size; 
}

char* Board::fen(){
  std::string r = "";
  for(int i = size-1; i >= 0; --i){ 
    std::string tmp = ""; 
    if(queens[i].y >= 1){ 
      tmp += std::to_string(queens[i].y) + 'Q'; 
      if (((size - queens[i].y)-1) > 0)
        tmp += std::to_string(size - queens[i].y - 1); 
    } else
      tmp += 'Q' + std::to_string(size-queens[i].y - 1); 
    if(i-1 >= 0) tmp += '/';
    r += tmp; 
  }
  char* ret = new char[r.length()];  
  for(int i =0; i < r.length(); ++i) 
    ret[i] = r[i];
  return ret;  
}


extern "C"{ 
  Board* new_board(int x, int y, int size=8){return new Board(x, y, size);}

  void display_board(Board* b){b -> display();}

  char* fen_formatter(Board* b){
    return b -> fen(); 
  }
}