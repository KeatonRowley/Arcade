package battleShip;

import java.util.Scanner;

public class Ship {
	
	Boolean hit = false;
	Location[] loc;
	int life;
	
	Ship(int size){
		hit = false;
		loc = new Location[size];
		life = size;
	}
		
	public Boolean checkLife() {
		return life > 0;
	}
	
	public static void setShip(Board brd_, Ship ship_) {
		
	}
	
	public static String getShipLocation(Scanner input) {
		String str = input.nextLine();
		while(str == null || str.equals("") ) {
			System.err.print("Bad input, input desired ship location (A#-A#): ");
			str = input.nextLine();
		}
		return str;
	}
	
}
