
class Box {            //class_name should be Capital
int ln,bd,hg;
public void set(int l, int b, int h){
ln=l;
bd=b;
hg=h;
}
public void show(){
System.out.println(ln);
System.out.println(bd);
System.out.println(hg);
}}

public class Exe {
public static void main(String[] args){  //String should be capital
Box bx = new Box();
bx.set(12,5,8);
bx.show();
}}
