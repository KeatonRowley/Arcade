package battleShip;

/**
 * 
 * @author Keaton.Evans
 * @Date 5/11/2018
 * 
 * This class holds coordinates for battleship points. It contains two constructors.
 * One can initialize a location with integers, and teh other with a sent char for the row
 * and a int for the height.
 */
public class Location {
	int row, height;
	
	Location(int row_, int height_) {	
		row = row_;
		height = height_;
	}
	Location(char row_, int height_){
		row = translation(row_);
		height = height_;
	}
	
	/**
	 * 
	 * @param ch is translated into a numeric equivalent.
	 * @return returns the int representation of ch. 
	 */
	public static int translation(char ch){
		String tranString = "" +ch;
		if(tranString.toUpperCase().equals("A"))
			return 0;
		else if(tranString.toUpperCase().equals("B"))
			return 1;
		else if(tranString.toUpperCase().equals("C"))
			return 2;
		else if(tranString.toUpperCase().equals("D"))
			return 3;
		else if(tranString.toUpperCase().equals("E"))
			return 4;
		else if(tranString.toUpperCase().equals("F"))
			return 5;
		else if(tranString.toUpperCase().equals("G"))
			return 6;
		else if(tranString.toUpperCase().equals("H"))
			return 7;
		else if(tranString.toUpperCase().equals("I"))
			return 8;
		else if(tranString.toUpperCase().equals("J"))
			return 9;
		else return -1;
	}
}
