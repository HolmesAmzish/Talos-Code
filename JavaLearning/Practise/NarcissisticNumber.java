/**
 * program: Narcissistic Number
 * date: 2024.07.23
 * author: Nulla
 */

public class NarcissisticNumber {
	public static void main(String[] args) {
		int numOfNarcissisticNumber = 0;
		for (int i = 100; i < 1000; i++) {
			int digital1 = i % 10;
			int digital2 = i /10 % 10;
			int digital3 = i / 100;
			if (Math.pow(digital1, 3) + Math.pow(digital2, 3) + Math.pow(digital3, 3) == i) {
				System.out.println("Narcisststic Number found: " + i);
				numOfNarcissisticNumber++;
			}
		}
		System.out.println("The number of narssistic number is: " + numOfNarcissisticNumber);
	}
}
 
