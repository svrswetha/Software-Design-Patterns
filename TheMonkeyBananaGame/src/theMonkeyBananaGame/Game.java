package theMonkeyBananaGame;

import java.awt.Color;
import java.awt.Dimension;
import java.awt.Graphics;
import java.awt.Graphics2D;
import java.awt.Image;
import java.awt.event.ActionEvent;
import java.awt.event.ActionListener;
import java.awt.event.KeyEvent;
import java.awt.event.KeyListener;
import java.io.BufferedInputStream;
import javax.sound.sampled.AudioInputStream;
import javax.sound.sampled.AudioSystem;
import javax.sound.sampled.Clip;
import javax.swing.ImageIcon;
import javax.swing.JPanel;
import javax.swing.Timer;

public class Game extends JPanel implements ActionListener, KeyListener {

	/**
	 * 
	 */
	private static final long serialVersionUID = 1L;

	// total game time
	private int gameTime = 50000;
	// time for banana re-birth :P
	private int bananaTime = 10000;

	private String successMessage = " :) HURRAY MONKEY WINS :)";
	private String failuresMessage = "POOR MONKEY :( TRY AGAIN";
	private String scoreMessage = "YOUR SCORE IS: ";

	private Image BananaScaling;
	private Image MonkeyScaling;

	private Graphics2D g2;

	private AudioInputStream gameOverAudioInputStream;

	private Clip gameOverClip;

	private boolean gameCompleted = false;

	private Monkey myMonkey;
	private Banana myBanana;

	// no of bananas which will make monkey full
	private int happyTarget = 5;

	private Timer bananaTimer, gameTimer;

	public void intializeSounds() {
		try {
			gameOverClip = AudioSystem.getClip();
			gameOverAudioInputStream = AudioSystem.getAudioInputStream(
					new BufferedInputStream(this.getClass().getResourceAsStream("/sounds/gameOverSound.wav")));
			gameOverClip.open(gameOverAudioInputStream);

		} catch (Exception e) {
			// TODO: handle exception
			e.printStackTrace();
			System.out.println("unable to play game sounds");
		}

	}

	/* Game Starts */
	Game() {

///*		initializing monkey and banana*/
		
		myMonkey = new Monkey();
		myBanana = new Banana();

//		adding key lsitners
		
		addKeyListener(this);
		setFocusable(true);
		
		this.setBackground(new Color(7, 145, 30));
		setFocusTraversalKeysEnabled(false);

//		loading images
		ImagesLoading();
		intializeSounds();

//		setting window size
		setPreferredSize(new Dimension(500, 500));

//		registering callback listeners for game and banana timeout
		ActionListener bananaListener = registerBananaListner();
		ActionListener gameListener = registerGameListner();

// 		starting timers		
		startBananaTimer(bananaListener, bananaTime);
		startGameTimer(gameListener, gameTime);

		// to put changes to effect
		repaint();
	}

	private void startBananaTimer(ActionListener bananaListener, int bananaTime) {
		bananaTimer = new Timer(bananaTime, bananaListener);
		bananaTimer.start();
	}

	private void startGameTimer(ActionListener gameListener, int gameTime) {
		gameTimer = new Timer(gameTime, gameListener);
		gameTimer.start();
	}

	private ActionListener registerGameListner() {
		// TODO Auto-generated method stub
		ActionListener gameListener = new ActionListener() {

			@Override
			public void actionPerformed(ActionEvent arg0) {
				gameOver();
				repaint();
			}
		};
		return gameListener;
	}

	private ActionListener registerBananaListner() {
		// TODO Auto-generated method stub
		ActionListener bananaListener = new ActionListener() {
			@Override
			public void actionPerformed(ActionEvent arg0) {

				updateBananaLocation();
				myMonkey.playMissedBananaClip();

				repaint();
			}
		};
		return bananaListener;

	}

	/* Game Time ends when Game is Over */
	public void gameOver() {
		gameCompleted = true;

		bananaTimer.stop();
		gameTimer.stop();

		gameOverClip.stop();
		gameOverClip.setMicrosecondPosition(0);
		gameOverClip.start();

		removeKeyListener(this);

	}

	/* Monkey and Banana Images are Loaded in the WonderLand */
	public void ImagesLoading() {

		ImageIcon BananaImage = myBanana.getBananaImageIcon();
		BananaScaling = BananaImage.getImage().getScaledInstance(50, 50, java.awt.Image.SCALE_SMOOTH);

		ImageIcon MonkeyImage = myMonkey.getMonkeyImageIcon();
		MonkeyScaling = MonkeyImage.getImage().getScaledInstance(50, 50, java.awt.Image.SCALE_SMOOTH);

	}

	@Override
	public void paintComponent(Graphics g) {

		super.paintComponent(g);

		if (gameCompleted) {
			setBackground(Color.WHITE);
			if (myMonkey.isMonkeyFull(happyTarget)) {
				g.drawString(scoreMessage + Integer.toString(myMonkey.getHappyCount()), 250, 250);
				g.drawString(successMessage, 250, 200);

			} else {
				g.drawString(scoreMessage + Integer.toString(myMonkey.getHappyCount()), 250, 250);
				g.drawString(failuresMessage, 250, 200);
			}

		} else {
			g2 = (Graphics2D) g;
			g2.drawImage(BananaScaling, myBanana.getGlobalBananaX(), myBanana.getGlobalBananaY(), this);
			g2.drawImage(MonkeyScaling, myMonkey.getGlobalMonkeyX(), myMonkey.getGlobalMonkeyY(), this);
			g2.drawString(Integer.toString(myMonkey.getHappyCount()), 450, 50);
			g2.dispose();
		}
	}

	/* check if the monkey is full and update the game status */
	public void checkUpdateHappyMonkey() {
		if (myMonkey.isMonkeyHappy(myBanana.getGlobalBananaX(), myBanana.getGlobalBananaY())) {
			this.updateBananaLocation();
			myMonkey.playHappyClip();
		}
		if (myMonkey.isMonkeyFull(happyTarget)) {
			gameOver();
		}
	}

	/* Banana is placed at another randomly determined position */
	public void updateBananaLocation() {

		int randomX = (int) (Math.random() * 10);
		int randomY = (int) (Math.random() * 10);
		randomX = randomX * 50;
		randomY = randomY * 50;
		myBanana.updateGlobalBananaPositions(randomX, randomY);
	}

	/*
	 * When the up,down,left,right keys are pressed, keyPressed() is invoked and act
	 * accordingly
	 */
	@Override
	public void keyPressed(KeyEvent e) {
		int code = e.getKeyCode();
		if (code == KeyEvent.VK_UP) {
			myMonkey.monkeyStateUp();
			checkUpdateHappyMonkey();
			movementLog();
			repaint();
		}
		if (code == KeyEvent.VK_DOWN) {
			myMonkey.monkeyStateDown();
			checkUpdateHappyMonkey();
			movementLog();
			repaint();
		}
		if (code == KeyEvent.VK_RIGHT) {
			myMonkey.monkeyStateRight();
			checkUpdateHappyMonkey();
			movementLog();
			repaint();
		}
		if (code == KeyEvent.VK_LEFT) {
			myMonkey.monkeyStateLeft();
			checkUpdateHappyMonkey();
			movementLog();
			repaint();
		}

	}

	@Override
	public void keyTyped(KeyEvent e) {
	}

	@Override
	public void keyReleased(KeyEvent arg0) {
		// TODO Auto-generated method stub

	}

	@Override
	public void actionPerformed(ActionEvent arg0) {
		// TODO Auto-generated method stub }

	}

	/*
	 * Monkey and Banana Movements are logged in order to visualize when monkey gets
	 * the banana
	 */
	public void movementLog() {
		System.out.println("monkey" + myMonkey.getGlobalMonkeyX() + "," + myMonkey.getGlobalMonkeyY());
		System.out.println("banana" + myBanana.getGlobalBananaX() + "," + myBanana.getGlobalBananaY());
	}

}
