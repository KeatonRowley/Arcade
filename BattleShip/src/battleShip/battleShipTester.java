package battleShip;

import static org.junit.Assert.*;

import java.io.IOException;
import java.util.Scanner;

import org.junit.Test;

public class battleShipTester {

	@Test
	public void welcomeToBattleShipVisual() {
		Display.welcomeToBattleship();
	}
	
	@Test
	public void youWinVisual() {
		Display.youWin();
	}
	
	@Test
	public void computerWinVisual() {
		Display.computerWin();
	}

	@Test
	public void hitVisual() {
		Display.hit();
	}
	
	@Test
	public void computerHitVisual() {
		Display.computerHit();
	}
	
	@Test
	public void yourShipSunkVisual() {
		Display.yourShipSunk();
	}
	
	@Test
	public void missVisual() {
		Display.miss();
	}
	
	@Test
	public void locationInitializationIntRowIntHeight() {
		Location coordinate = new Location(0,5);
		assertTrue(coordinate.row == 0 && coordinate.height == 5);  
	}
	
	@Test
	public void locationInitializationCharRowIntHeight() {
		Location coordinate = new Location('b',5);
		assertTrue(coordinate.row == 1 && coordinate.height == 5);  
	}
	
	@Test
	public void locationInitializationCharRowIntHeightOutOfBounds() {
		Location coordinate = new Location('k',5);
		assertTrue(coordinate.row == -1 && coordinate.height == 5);  
	}
	
	@Test
	public void initializeBoard() {
		Board brd = new Board("Keaton");
		assertTrue(brd.name.equals("Keaton"));
	}
	
	@Test
	public void displayBoard() {
		Board brd = new Board("Keaton");
		Display.displayBoard(brd);
	}
	
	@Test
	public void displayGame() {
		Board brd1 = new Board("Keaton");
		Board brd2 = new Board("Rowley");
		Game game1 = new Game(brd1, brd2);
		Display.displayGame(game1);
	}
	
	@Test
	public void displayGameLongName() {
		Board brd1 = new Board("SuperliciousAllDelicious");
		Board brd2 = new Board("PineApplesRSShippedByUPS");
		Game game1 = new Game(brd1, brd2);
		Display.displayGame(game1);
	}
	
	@Test
	public void displayGameVeryLongName() {
		Board brd1 = new Board("SuperliciousAllDeliciousDironisourusReximus");
		Board brd2 = new Board("PineApplesRSShippedByUPSTeridactylSupistar");
		Game game1 = new Game(brd1, brd2);
		Display.displayGame(game1);
	}
	
	

	
	
}
