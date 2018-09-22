#In.Dec.
public class Program {
    public static void main(String[] args) {
        int a = 33;
        int b = --a; //32
        int c = a--; //32
        int d = ++a; //32
        int e = a++; //32
        int f = a;   //33

        System.out.println(b+"\n"+c+"\n"+d+"\n"+e+"\n"+f);
    }
}

