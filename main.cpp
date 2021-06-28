#include <iostream> 
using namespace std; 

void display_board(){ 

    int size = 8;

    for(int i = 0; i < size; i++){ 
        if (i == 0) cout << "  "; 
        cout << i + 1 << ' ';
    } 
        
    cout << endl; 
    for(int x = 0; x < size; x++){ 
        cout << x + 1 << " * "; 
        for (int y = 0; y < size-1; y++){ 
            cout << "* "; 
        }
        cout << endl; 
    }

    return; 
}

int main(){ 

    display_board(); 

    return 0; 
}