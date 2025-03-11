import java.util.Scanner;

/*
 *  Max number (base 10) 999999999
 */

public class baseConverter {
    public static void main(String[] args) {
        int num;

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Gib eine Zahl an: ");
            num = scanner.nextInt();
        }
        for (int i = 2; i <= 36; i++) {
            System.out.println("Die gegebene Zahl in Basis " + i + ": " + toBase(num, i));
        }
    }

    public static void second(String[] args) {
        int i = 25;
        int num = 28;
        System.out.println("Die gegebene Zahl in Basis " + i + ": " + toBase(num, i));
    }

    public static String toBase(int num, int base) {
        if (num == 0) return "0";
        if (num < base) return hexChar(num);
        return toBase(num / base, base) + hexChar(num % base);
    }

    private static String hexChar(int remainder) {
        return "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ".charAt(remainder) + "";
    }
}