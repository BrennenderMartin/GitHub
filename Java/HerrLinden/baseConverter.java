import java.util.Scanner;

public class baseConverter {
    public static void main(String[] args) {
        int num;
        int base = 2;

        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Gib eine Zahl an: ");
            num = scanner.nextInt();
        }
        
        for (int i = base; i <= 16; i++) {
            System.out.println("Die gegebene Zahl in Basis " + i + ": " + toBase(num, i));
        }
    }

    public static String toBase(int num, int base) {
        if (num == 0) return "0";
        if (num < base) return hexChar(num);
        return toBase(num / base, base) + hexChar(num % base);
    }

    private static String hexChar(int remainder) {
        return "0123456789ABCDEF".charAt(remainder) + "";
    }
}