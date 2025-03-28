package Konto;

public class Object implements Account {
    private double attr;
    private String name;

    // Constructor with name and attribute
    public Object(String name, double attribute) {
        this.name = name;
        this.attr = attribute;
    }

    // Constructor with name only; defaults attribute to 0.0
    public Object(String name) {
        this(name, 0.0);
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