/**
 * program: Random Number
 * date: 2024.07.24
 * author: nulla
 */

import java.util.Random;
import java.util.Scanner;

public class RandomNumber {
	public static void main(String[] args) {
		Random rd = new Random();
		int randomNumber = rd.nextInt(100) + 1;
		while (true) {
			Scanner sc = new Scanner(System.in);
			System.out.print("Please entye a number: ");
			int input = sc.nextInt();
			if (input == randomNumber) {
				System.out.println("Congratulations! You guessed right number!");
				break;
			} else if (input < randomNumber) {
				System.out.println("Wrong answer, enter a larger number.");
			} else {
				System.out.println("Wrong answer, enter a smaller number.");
			}
		}
	}
}


