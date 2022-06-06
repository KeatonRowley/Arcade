package battleShip;

public class Game {
	Board player1;
	Board player2;
	Boolean gameWon;
	ChooseFunctor play1Funct;
	ChooseFunctor play2Funct;
	
	Game(Board play1, Board play2, ChooseFunctor play1Funct_, ChooseFunctor play2Funct_){
		player1 = play1;
		player2 = play2;
		play1Funct = play1Funct_;
		play2Funct = play2Funct_;
		gameWon = false;
	}
}
