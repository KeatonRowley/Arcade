package battleShip;

import java.util.Scanner;

public class Run {
	public static void main(String[] args) {
		Boolean playAgain = true;
		Boolean playComputer = false;
		char choice = 'C';
		Scanner input = new Scanner(System.in);
		
		Display.welcomeToBattleship();	// display battleship logo.
		
		while(playAgain) {
			System.out.println("Welcome to Battleship! Which mode would you "
					+ "like to play? (Type A or B)");	// tell player their options.
			System.out.println("A: 2-player");
			System.out.println("B: Play computer");
			System.out.print("Mode: ");
			
	
			choice = getCharInput(input);
			
			while(choice != 'A' && choice != 'B' 					// validate input
					&& choice != 'a' && choice != 'A') { 
				System.out.println("You must either type A or B");
				System.out.print("Mode: ");
				choice = getCharInput(input);
			}
			
		if(choice == 'B' || choice == 'b')
				playComputer = true;
			
			if(playComputer)
				System.out.println("I'm playing the computer!");
			else if(!playComputer)
				System.out.println("I'm playing with 2 people!");	
			
			System.out.print("Would you like to play again? (y or n): ");
			
			
			choice = getCharInput(input);
			playAgain = (choice== 'Y' || choice == 'y') ? true: false;	// checks want play again.
		
		}
		
		
		
	}
	
	public static Game twoPlayerSetUp() {
		Scanner input = new Scanner(System.in);
		System.out.println("Enter player1 name: ");
		String player1 = getName(input);
		System.out.println("Enter player2 name: ");
		
		String player2 = getName(input);
		Board play1Board = setBoard(player1);
		Board play2Board = setBoard(player2);
		ChooseFunctor functor = new ChooseFunctor.twoPlayerFunctor();
		return new Game(play1Board, play2Board, functor, functor);
		
	}
	
	public static Board setBoard(String name) {
		return new Board();
	}
	/**
	 * This returns a ch input by the user, checks for bad input.
	 * @param input scanner used.
	 * @return Returns a ch.
	 */
	
	private static char getCharInput(Scanner input) {
		String str = input.nextLine();
		while(str == null || str.equals("") ) {
			System.err.print("Bad input, input character: ");
			str = input.nextLine();
		}
		return str.charAt(0);
	}
	
	private static String getName(Scanner input) {
		String str = input.nextLine();
		while(str == null || str.equals("") ) {
			System.err.print("Bad input, input character: ");
			str = input.nextLine();
		}
		return str;
	}
	
} // End of file.
