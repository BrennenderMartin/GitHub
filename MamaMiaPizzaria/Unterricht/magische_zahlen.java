import java.util.Scanner;

public class magische_zahlen {
    int var;
    
    public static void main(String[] args) {
        new magische_zahlen();
    }

    private magische_zahlen() {
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Gib mir eine Variable und ich errate diese: ");
            var = scanner.nextInt();
        }
        System.out.println("The given variable is: " + var);
        exe(var);
    }

    public void exe(int var) {
        switch (var) {
            case 1: System.out.println("Variable is 1"); break;
            case 2: System.out.println("Vairable is 2"); break;
            default: System.out.println("Variable is less than 1 or more than 2");
        }
    }
}
