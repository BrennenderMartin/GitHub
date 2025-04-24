package Konto;

import java.util.Scanner;

public class User {
    public static void main(String[] args) {
        try (Scanner scanner = new Scanner(System.in)) {
            /*System.out.println("text");
            var = scanner.nextInt();*/
            int counter = 0;
            boolean running = true;
            while (running) {
                System.out.println("Please enter a command:\n" +
                        "1. exit\n" +
                        "2. create an account\n" +
                        "3. deposit\n" +
                        "4. withdraw\n" +
                        "5. help");
                String command = scanner.nextLine();
                switch (command) {
                    case "1":
                        System.out.println("Exiting...");
                        running = false;
                        break;
                    case "2":
                        System.out.println("Creating an account...");
                        System.out.println("Please enter the account name:");
                        String name = scanner.nextLine();
                        System.out.println("Please enter the initial amount:");
                        double amount = scanner.nextDouble();
                        scanner.nextLine();
                        Object account = new Object(name, amount);
                        System.out.println("Account created: " + account);
                        break;
                    case "3":
                        System.out.println("Depositing...");
                        System.out.println("Please enter the account name:");
                        String depositName = scanner.nextLine();
                        System.out.println("Please enter the amount to deposit:");
                        double depositAmount = scanner.nextDouble();
                        scanner.nextLine();
                        // Assuming you have a method to find the account by name
                        // Object accountToDeposit = findAccountByName(depositName);
                        // accountToDeposit.deposit(depositAmount);
                        System.out.println("Deposited " + depositAmount + " into " + depositName);
                        break;
                    case "4":
                        System.out.println("Withdrawing...");
                        System.out.println("Please enter the account name:");
                        String withdrawName = scanner.nextLine();
                        System.out.println("Please enter the amount to withdraw:");
                        double withdrawAmount = scanner.nextDouble();
                        scanner.nextLine();
                        // Assuming you have a method to find the account by name
                        // Object accountToWithdraw = findAccountByName(withdrawName);
                        // accountToWithdraw.withdraw(withdrawAmount);
                        System.out.println("Withdrew " + withdrawAmount + " from " + withdrawName);
                        break;
                    case "5":
                        System.out.println("Help:");
                        System.out.println("1. exit - Exit the program");
                        System.out.println("2. create an account - Create a new account");
                        System.out.println("3. deposit - Deposit money into an account");
                        System.out.println("4. withdraw - Withdraw money from an account");
                        System.out.println("5. help - Show this help message");
                        break;
                    default:
                        counter++;
                        if ( counter > 3) {
                            System.out.println("Too many invalid attempts. Exiting...");
                            running = false;
                        } else {
                            System.out.println("Unknown command. Please try again.");
                        }
                        break;
                }
            }
        }
    }
}
