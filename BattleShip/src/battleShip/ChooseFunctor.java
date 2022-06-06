package battleShip;

public interface ChooseFunctor {

	public Location fire(Board brd);
	
	public class twoPlayerFunctor implements ChooseFunctor {
		public Location fire(Board brd) {
			return new Location(0,0);
		}
	}
	public class randomChoiceFunctor implements ChooseFunctor{
		public Location fire(Board brd) {
			return new Location(0,0);
		}
	}
	public class halfBoardTargetingFunctor implements ChooseFunctor{
		public Location fire(Board brd) {
			return new Location(0,0);
		}
	}
	public class probabilityFunctor implements ChooseFunctor{
		public Location fire(Board brd) {
			return new Location(0,0);
		}
	}
}

