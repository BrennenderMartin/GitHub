package Pizza_Project;

/**
 * Same shit as MyObject, just renamed everything
 */
public class User {
    private String username;
    private String password;

    public User(String username, String password) {
        this.username = username;
        this.password = password;
    }

    public static void main(String[] args) {
        User user = new User("admin", "1234");
        System.out.println(user);
    }

    public String getUsername() {
        return username;
    }

    public String getPassword() {
        return password;
    }

    public void setUsername(String username) {
        this.username = username;
    }

    public void setPassword(String password) {
        this.password = password;
    }

    @Override
    public boolean equals(Object obj) {
        if (this == obj) return true;
        if (obj == null || getClass() != obj.getClass()) return false;
        User user = (User) obj;
        return username.equals(user.username);
    }
    
    @Override
    public String toString() {
        return "Username: " + username + ", Password: " + password;
    }

    //@Override
    public int hashCode() {
        return username.hashCode();
    }
}
