package theMonkeyBananaGame;

import javax.swing.JFrame;
import javax.swing.WindowConstants;

public class Main {

	public static void main(String[] args) {
		JFrame f = new JFrame("MONKEY-BANANA GAME");
     	Game m = new Game();
		f.add(m);
		f.setSize(500,500);
		f.setResizable(false);
		f.setVisible(true);
		f.setDefaultCloseOperation(WindowConstants.EXIT_ON_CLOSE);
	}

}
