package theMonkeyBananaGame;

import java.io.BufferedInputStream;

import javax.imageio.ImageIO;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.ImageIcon;

public class Monkey {
	
	private AudioInputStream happyAudioInputStream , missedAudioInputStream;
	private Clip happyClip, missedBananaClip;

	private ImageIcon monkeyImageIcon;
	
	private int globalHappyCount;
	
	private int globalVelocityX,globalVelocityY;

	private int deltaX,deltaY;

	private int globalMonkeyX,globalMonkeyY;

	private void initResources() {
		try {
			
		 happyClip = AudioSystem.getClip();
		 happyAudioInputStream = AudioSystem.getAudioInputStream(new BufferedInputStream(this.getClass().getResourceAsStream("/sounds/monkeyHappy.wav")));
		 happyClip.open(happyAudioInputStream);
		 
		 missedBananaClip = AudioSystem.getClip();
		 missedAudioInputStream = AudioSystem.getAudioInputStream(new BufferedInputStream(this.getClass().getResourceAsStream("/sounds/missedBanana.wav")));
		 missedBananaClip.open(missedAudioInputStream);
		 
		 monkeyImageIcon = new ImageIcon(ImageIO.read(new BufferedInputStream(this.getClass().getResourceAsStream("/avatars/monkey.png"))));

		 
		}catch(Exception e) {
			System.out.println("unable to init monkey resources");
			e.printStackTrace();
		}
	}
	
	
	public ImageIcon getMonkeyImageIcon() {
		return monkeyImageIcon;
	}
	
	public void playHappyClip() {
		happyClip.stop();
		happyClip.setMicrosecondPosition(0);
		happyClip.start();
		
	}
	public void playMissedBananaClip() {
		missedBananaClip.stop();
		missedBananaClip.setMicrosecondPosition(0);
		missedBananaClip.start();
	}
	
	
	public Monkey() {
		this.globalHappyCount = 0;
		this.globalVelocityX = 10;
		this.globalVelocityY = 10;
		this.deltaX =20;
		this.deltaY =25;
		this.globalMonkeyX = 100;
		this.globalMonkeyY = 200;
		 initResources();
		}
	public Monkey(int customHappyCount) {
		this.globalHappyCount = customHappyCount;
		this.globalVelocityX = 10;
		this.globalVelocityY = 10;
		this.deltaX =20;
		this.deltaY =25;
		this.globalMonkeyX = 100;
		this.globalMonkeyY = 200;
		
		initResources();
	}
	
	
	public Monkey(int customHappyCount, int customVelocityX, int customVelocityY,int monkeyX,int monkeyY) {
		this.globalHappyCount = customHappyCount;
		this.globalVelocityX = customVelocityX;
		this.globalVelocityY = customVelocityY;
		
		this.globalMonkeyX = monkeyX;
		this.globalMonkeyY = monkeyY;
		
		this.deltaX =20;
		this.deltaY =25;
		
		initResources();
		
	}
	
	public Monkey(int customHappyCount, int customVelocityX, int customVelocityY,
			int customDeltaX, int customDeltaY,int monkeyX,int monkeyY) {
		this.globalHappyCount = customHappyCount;
		this.globalVelocityX = customVelocityX;
		this.globalVelocityY = customVelocityY;
		
		this.deltaX = customDeltaX;
		this.deltaY = customDeltaY;
		
		this.globalMonkeyX = monkeyX;
		this.globalMonkeyY = monkeyY;
		
		initResources();
		

	}



	private void setGlobalMonkeyX(int globalMonkeyX) {
		this.globalMonkeyX = globalMonkeyX;
	}
	private void setGlobalMonkeyY(int globalMonkeyY) {
		this.globalMonkeyY = globalMonkeyY;
	}

	public int getHappyCount() {
		return globalHappyCount;
	}

	private int getGlobalHappyCount() {
		return globalHappyCount;
	}
	private void setGlobalHappyCount(int globalHappyCount) {
		this.globalHappyCount = globalHappyCount;
	}


	private void updateHappyCount() {
		this.setGlobalHappyCount(this.getGlobalHappyCount()+1);
	}

	
	
	public int getGlobalMonkeyX() {
		return globalMonkeyX;
	}

	public int getGlobalMonkeyY() {
		return globalMonkeyY;
	}


	public void updateGlobalMonkeyPositions(int monkeyX,int monkeyY) {
		globalMonkeyX = monkeyX;
		globalMonkeyY = monkeyY;
	}
	
	public boolean isMonkeyFull(int happyTarget) {
		if(this.getGlobalHappyCount() >= happyTarget) {
			return true;
		} return false;
	}
	
	/* isMonkeyHappy checks whether Monkey successfully gets and eats the banana */
	public boolean isMonkeyHappy(int bananaX, int bananaY) {
		if(((this.getGlobalMonkeyX() >= bananaX - deltaX) && (this.getGlobalMonkeyX() <= bananaX + deltaX)) 
				&& ((this.getGlobalMonkeyY()  >= bananaY - deltaY) && (this.getGlobalMonkeyY() <= bananaY + deltaY))) {
			
			updateHappyCount();
			
			return true;	
		}
		return false;
	}
	
/* Monkey States: Monkey can move horizontally and Vertically controlled by up,down,left,right keys of the keyboard */

	public void monkeyStateUp() {

		this.setGlobalMonkeyY(this.getGlobalMonkeyY()-globalVelocityY);
		movementLog();
	}
	
	public void monkeyStateDown() {
		
		this.setGlobalMonkeyY(this.getGlobalMonkeyY()+globalVelocityY);
		movementLog();
	}
	
	public void monkeyStateLeft(){
		this.setGlobalMonkeyX(this.getGlobalMonkeyX()-globalVelocityX);
		movementLog();
	}
	

	public void monkeyStateRight() {
		this.setGlobalMonkeyX(this.getGlobalMonkeyX()+globalVelocityX);
		movementLog();
	}
	
	private void movementLog() {
	    System.out.println("monkey"+this.getGlobalMonkeyX()+","+this.getGlobalMonkeyY());
	}


}
