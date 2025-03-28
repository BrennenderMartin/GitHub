package Konto;

// Added interface to encapsulate account operations
interface Account {
    // Returns the current attribute (e.g. balance)
    double getAttribute();

    // Sets the attribute value
    void setAttribute(double attribute);

    // Increases the attribute by amount
    void deposit(double amount);

    // Decreases the attribute by amount
    void withdraw(double amount);
}

class Object implements Account {
    private double attr;
    private String name;

    public Object(String name, double attr) {
        this.name = name;
        this.attr = attr;
    }

    public Object(String name) {
        this.name = name;
        this.attr = 0.0;
    }

    public double getAttribute() {
        return attr;
    }

    public void setAttribute(double attribute) {
        this.attr = attribute;
    }

    public void deposit(double amount) {
        this.attr += amount;
    }

    public void withdraw(double amount) {
        this.attr -= amount;
    }

    public String toString() {
        return name + ": " + attr;
    }
}

public class User {
    public static void main(String[] args) {
        Account account = new Object("Klaus", 420.69);
        System.out.println(account);
    }

    public static void createAccount(String name, double attribute) {
        Account account = new Object(name, attribute);
    }

    public static void createAccount(String name) {
        Account account = new Object(name);
    }

    public static void getAttribute(Account account) {
        System.out.println(account.getAttribute());
    }

    public static void setAttribute(Account account, double attribute) {
        account.setAttribute(attribute);
    }

    public static void deposit(Account account, double amount) {
        account.deposit(amount);
    }

    public static void withdraw(Account account, double amount) {
        account.withdraw(amount);
    }

    public static void transfer(Account sender, Account receiver, double amount) {
        sender.setAttribute(sender.getAttribute() - amount);
        receiver.setAttribute(receiver.getAttribute() + amount);
    }
}
