package theMonkeyBananaGame;

import java.io.BufferedInputStream;

import javax.imageio.ImageIO;
import javax.swing.ImageIcon;

public class Banana {
	
	private int globalBananaX,globalBananaY;
	private ImageIcon bananaImageIcon;
	
	
	
	public Banana(int globalBananaX, int globalBananaY) {
		this.globalBananaX = globalBananaX;
		this.globalBananaY = globalBananaY;
		initResources();
	}

	
	public Banana() {
		this.globalBananaX = 20;
		this.globalBananaY = 100;
		initResources();
	}
	
	
	public void updateGlobalBananaPositions(int bananaX,int bananaY) {
		this.globalBananaX = bananaX;
		this.globalBananaY = bananaY;
	}

	public int getGlobalBananaX() {
		return globalBananaX;
	}

	public int getGlobalBananaY() {
		return globalBananaY;
	}

	public ImageIcon getBananaImageIcon() {
		return bananaImageIcon;
	}

	
	private void initResources() {
		try {
			bananaImageIcon = new ImageIcon(ImageIO.read(new BufferedInputStream(this.getClass().getResourceAsStream("/avatars/HappyBanana.png"))));
		}catch (Exception e) {
			// TODO: handle exception
			System.out.println("unable to init banana resources");
			e.printStackTrace();
		}
	}


}
