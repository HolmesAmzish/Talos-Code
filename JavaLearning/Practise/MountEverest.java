/**
 * program: Mount Everest
 * date: 2024.07.23
 * author: nulla
 */

public class MountEverest {
	public static void main(String[] args) {
		float hight = 0.1f;
		int times = 0;
		while (hight < 8844430) {
			hight *= 2;
			times++;
		}
		System.out.println("The number of times is: " + times);
	}
}
