import java.util.Scanner;

public class magische_zahlen {
    int var;
    int max;

    public static void main(String[] args) {
        new magische_zahlen();
    }

    private magische_zahlen() {
        max = 100;
        try (Scanner scanner = new Scanner(System.in)) {
            System.out.println("Gib mir eine Zahl zwischen 1 und " + max + " und ich errate diese: ");
            var = scanner.nextInt();
        }
        System.out.println("The given variable is: " + var);
        exe(var);
    }

    public void ex2(int var) { //Binary search
        @SuppressWarnings("unused")
        int min = 0;
        int middle = max / 2;
        if (var == middle) {
            System.out.println("Die Zahl von dir ist: " + var);
        }else if(var < middle) {
            max = middle;
        }else if(var > middle) {
            min = middle;
        }
    }
    public void exe(int var) {
        switch (var) {
            case 1: System.out.println("Variable is 1"); break;
            case 2: System.out.println("Vairable is 2"); break;
            default: System.out.println("Variable is less than 1 or more than 2");
        }
    }
}
