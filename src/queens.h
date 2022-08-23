#include <string> 
#include <vector> 

struct Point{ 
  public: 
    int x, y; 
    bool queen, safe; 
    Point(int, int, bool, bool); 
    Point(){};  
    inline std::string str() const; 
    inline std::string raw() const; 
}; 


class Board{ 
  public:
    Board(int, int, int);    
    bool scan(std::vector<std::vector<Point> > const&, int=0, int=0); 
    void display();
    char* formatter(); 
    inline std::vector<std::vector<Point> > getBoard() const; 
    inline int getSize() const noexcept; 
  private: 
    void set(int, int);
    int size;    
    std::vector<std::vector<Point> > cb;  //chessboard 
    Point queen;   
};    
