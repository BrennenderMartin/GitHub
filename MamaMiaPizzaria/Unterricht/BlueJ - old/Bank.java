
/**
 * Write a description of class Bank here.
 *
 * @author (your name)
 * @version (a version number or a date)
 */
public class Bank
{
    // instance variables - replace the example below with your own
    int muenzen;

    /**
     * Constructor for objects of class Bank
     */
    public Bank()
    {
        // initialise instance variables
        muenzen = 0;
        System.out.println("Die Bank hat " + muenzen + " Münzen");
    }

    /**
     * An example of a method - replace this comment with your own
     *
     * @param  y  a sample parameter for a method
     * @return    the sum of x and y
     */
    public void method(int augenzahl)
    {
        muenzen += augenzahl;
    }
}
