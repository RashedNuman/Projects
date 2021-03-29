#include <iostream>  // Imports
#include <random>

using namespace std;

// Declaring variables

static int win = 0;

// The X O grid 
char board[9] = { '?' ,  '?' ,  '?' ,  '?' ,  '?' ,  '?' ,  '?' ,  '?' , '?'};


/**
 * PVC (player vs computer)
 * void function with no parameters, initiates a round of tic tac
 * toe between the player and the bot, calls winner function to 
 * determine if someone won at the end of each round.
 * Bot's move is randomly generated with taken spots considered
 **/
 
 
void grid(){
     
    // Print X O grid each round
	for (int i = 0; i < 10; i++) 
	{

		if (i % 3 == 0) 
		{
		    cout << "\n";
		}

		cout << "\t";
		cout << board[i];

	}
 }
 
 void winner(char chr){

    int won;
  
     
    if ( board[0] == chr && board[3] == chr && board[6] == chr){ won = 1;}
    else if (board[1] == chr && board[4] == chr && board[7] == chr){ won = 1;}
    else if (board[2] == chr && board[5] == chr && board[8] == chr){ won = 1;}
    else if (board[0] == chr && board[4] == chr && board[8] == chr){ won = 1;}
    else if (board[2] == chr && board[4] == chr && board[6] == chr){ won = 1;}
    else if (board[0] == chr && board[1] == chr && board[2] == chr){ won = 1;}
    else if (board[3] == chr && board[4] == chr && board[5] == chr){ won = 1;}
    else if( board[6] == chr && board[7] == chr && board[8] == chr){ won = 1;}

    if ( won == 1 ){
        
        if ( chr == 'X'){ cout << "\n PLAYER 1 WON \n \n \n"; win++;}
        else if ( chr == 'O'){ cout << "\n PLAYER 2 WON \n \n \n"; win++;}
    }
         
 }
 
 
 
 
void PVC() {
    

	while (true) 
	{
		int loc;
        
        grid();
		
		// player turn in a infinite loop until he enters a valid
		// or untaken location on the grid

		while (true)
		{

			cout << "Enter Position : ";
			cin >> loc;

			if (loc > 9 || loc < 0)
			{
				cout << "Enter a valid position \n";
				continue;
			}

			if (board[loc] != '?') {

				cout << "This position is allready taken \n";
				continue;
			}
			
			// until the player's move is valid, the loop
			// will iterate again using continue

			break;
		}
        
        
        // placing the player's chosen location on the grid
		board[loc] = 'X';
		winner('X'); // check if X won

		if ( win == 1){ grid(); break;}
		
		// check if board is full before computer's turn
		// which also means it would be a draw
		
		int counter = 0;
		for ( int i = 0; i < 9; i++){
		    if (board[i] != '?'){
		        counter++;
		    }
		}
		
		if (counter == 9){
		    cout << "\n Its a draw... \n";
		    grid();
		    break;
		}
		
		
		
	
		// Bot's turn starts here
		int loc2;

		while (true)
		{
			
			
            // random integer from 0 to 9
			loc2 = 0 + (rand() % 9);
			cout << loc2;
			
			// if location is free, then put the O there
			// else use another spot thats not taken
			if (board[loc2] != '?') {
				continue;
			}
			else { board[loc2] = 'O'; break; }
		}
		
		
		
		
		winner('O'); // check if O won
		
		if ( win == 1){ grid(); break;}
		
	}
}






void PVP(){
    
    	while (true) 
	{
		int loc;
        
        grid();
		
		// player turn in a infinite loop until he enters a valid
		// or untaken location on the grid

		while (true)
		{

			cout << "Enter Position for player one : ";
			cin >> loc;

			if (loc > 9 || loc < 0)
			{
				cout << "Enter a valid position \n";
				continue;
			}

			if (board[loc] != '?') {

				cout << "This position is allready taken \n";
				continue;
			}
			
			// until the player's move is valid, the loop
			// will iterate again using continue

			break;
			
		}
		
        
        // placing the player's chosen location on the grid
		board[loc] = 'X';
		winner('X');
	    if ( win == 1){ grid(); break;}
		
		int loc2;
		
		while (true)
		{

			cout << "Enter Position for player two : ";
			cin >> loc2;

			if (loc2 > 8 || loc2 < 0)
			{
				cout << "Enter a valid position \n";
				continue;
			}

			if (board[loc2] != '?') {

				cout << "\n This position is allready taken \n";
				continue;
			}
			
			// until the player's move is valid, the loop
			// will iterate again using continue

			break;
			
		}
        
        // placing the player's chosen location on the grid
		board[loc2] = 'O';
		winner('O'); // check if O won
		if ( win == 1){ grid(); break;}
    }
}





int main()
{

	int choice;

	cout << " \t \t Welcome to Tic Tac Toe \n \n";
	
	
	while (true){
	    
	    cout << "\n Enter 1 for player vs PC or 2 for player vs player :  ";
	    cin >> choice;
	
	    if ( choice == 1){
	        PVC();
	    }
	    else if ( choice == 2){
	        PVP();
	
	    }
	    else{ cout << "\n Invalid choice \n";}
        
        // reseting the board and winner for next game
	   for ( int i = 0; i < 9; i++){board[i] = '?';}
	   win -=1;
	  
	
	}
}
