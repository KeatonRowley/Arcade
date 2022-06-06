package battleShip;

import java.util.Scanner;

public class Board {
	static Ship carrier;
	static Ship battleship;
	static Ship cruiser;
	static Ship sub;
	static Ship destroyer;
	static String name ;
	char board[][];
	
	Board() {
		carrier = new Ship(5);
		battleship = new Ship(4);
		cruiser = new Ship(3);
		sub = new Ship(3);
		destroyer = new Ship(2);
		name = "";
		board = new char[10][10];
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < 10; j++) {
				board[i][j] = '*';
			}
		}		
	}

	
	Board(String name_) {
		carrier = new Ship(5);
		battleship = new Ship(4);
		cruiser = new Ship(3);
		sub = new Ship(3);
		destroyer = new Ship(2);
		name = name_;
		board = new char[10][10];
		for(int i = 0; i < 10; i++) {
			for(int j = 0; j < 10; j++) {
				board[i][j] = '*';
			}
		}
	}
	
	public static Board setBoard(String name) {
		Boolean setCorrectly = false;
		Board brd = new Board(name);
		Scanner input = new Scanner(System.in);
		while(!setCorrectly) {
			Display.displayBoard(brd);
			System.out.println("Give location of where you would like to"
					+ " set your carrier (5-holes) as (A3-A7) or (B5-F5)");	
			shipInput(brd, Ship.getShipLocation(input), 5);
		}
		
		/*Ship.setShip(brd, Board.carrier); 
		Ship.setShip(brd, Board.battleship); 
		Ship.setShip(brd, Board.cruiser); 
		Ship.setShip(brd, Board.sub); 
		Ship.setShip(brd, Board.destroyer);*/
		
		return brd;
		
	}
	
	public static Boolean shipInput(Board brd, String str, int size) {
		if(str.length() < 5 ) 		// check to make sure string is long enough.
			return shipInputErr();
		
		
		int rowCoor = Location.translation(str.charAt(0));
		if(rowCoor < 0) 		// ensure letter coordinate is valid.
			return shipInputErr();

		String strIndex = "";			// translating first coordinate #
		int maxIndex = 1;
		for(int i = 1; str.charAt(i) != '-' || i < str.length(); i++, maxIndex++) {
			if(isCharInt(str.charAt(i)))
				strIndex += str.charAt(i);
			else shipInputErr();
		}
		if(strIndex.length()>2) 
			return shipInputErr();
		int locHeight = Integer.parseInt(strIndex);
		Location startLoc = new Location(rowCoor, locHeight);	// store coordinates as
																// a location
		strIndex = "";		// clear string
		
		rowCoor = Location.translation(str.charAt(maxIndex));	// get 2nd let coor.
		if(rowCoor < 0)
			return shipInputErr();
		for(int i = maxIndex;  i < str.length(); i++) {		// get 2nd # coordinate
			if(isCharInt(str.charAt(i)))
				strIndex += str.charAt(i);
			else shipInputErr();
		}
		
		if(strIndex.length()>2) 
			return shipInputErr();
		locHeight = Integer.parseInt(strIndex);
		Location endLoc = new Location(rowCoor, locHeight);
		
		if(startLoc.row == endLoc.height) {
			if(java.lang.Math.abs(startLoc.row-endLoc.height) != (size-1)) {
				System.out.println("You must give coordinates for a ship of size" 
						+size);
				return false;
			}
			for(int j = (startLoc.height >endLoc.height ? startLoc.height: endLoc.height); j < size; j++) {
				if()
			}
			
		}
		
			
	}
	
	public static Boolean shipInputErr() {
		System.out.println("Expected input is A#-C# or Letter#-Letter#.");
		return false;
	}
	
	public static Boolean isCharInt(char ch) {
		if(ch == '0')
			return true;
		else if(ch == '1')
				return true;
		else if(ch == '2')
			return true;
		else if(ch == '3')
			return true;
		else if(ch == '4')
			return true;
		else if(ch == '5')
			return true;
		else if(ch == '6')
			return true;
		else if(ch == '7')
			return true;
		else if(ch == '8')
			return true;
		else if(ch == '9')
			return true;
		else return false;
	}
	
	
}
