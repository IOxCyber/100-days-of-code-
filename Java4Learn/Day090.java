public class Vehicle {
    private String color;
    
    // Getter
    public String getColor() {
        return color;
    }
    
    // Setter
    public void setColor(String c) {
        this.color = c;
    }
}

class Program {
    public static void main(String[ ] args) {
        Vehicle v1 = new Vehicle();
        v1.setColor("Red");
        System.out.println(v1.getColor());
    }
}


/*
Getters and setters allow us to have control over the values. You may, for example, validate the given value in the setter before actually setting the value.

*/public class Vehicle {
    private String color;
    
    // Getter
    public String getColor() {
        return color;
    }
    
    // Setter
    public void setColor(String c) {
        this.color = c;
    }
}

class Program {
    public static void main(String[ ] args) {
        Vehicle v1 = new Vehicle();
        v1.setColor("Red");
        System.out.println(v1.getColor());
    }
}


/*
Getters and setters allow us to have control over the values. You may, for example, validate the given value in the setter before actually setting the value.



