package Pizza_Project;

/**
 * Class created by ChatGPT, to have a Object,
 * which can be compared in a list,
 * also used for the Speisekarte
 */
public class MyObject
{
    private String name;
    private double attribute;

    public MyObject(String name, double attribute) {
        this.name = name;
        this.attribute = attribute;
    }
    
    public MyObject(String name) {
        this.name = name;
        this.attribute = 0.0;
    }
    
    public static void main(String[] args) { //Just a small test how this method works
        MyObject object = new MyObject("Klaus", 420.69);
        System.out.println(object);
    }

    // Getter für den Namen
    public String getName() {
        return name;
    }

    // Getter für das Attribut
    public double getAttribute() {
        return attribute;
    }

    // Setter für den Namen
    public void setName(String name) {
        this.name = name;
    }

    // Setter für das Attribut
    public void setAttribute(double attribute) {
        this.attribute = attribute;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        MyObject myObject = (MyObject) obj;
        return name.equals(myObject.name);
    }
    
    @Override
    public String toString() {
        return "Name: " + name + ", Attribute: " + attribute;
    }

    //@Override
    public int hashCode() {
        return name.hashCode();
    }
}
