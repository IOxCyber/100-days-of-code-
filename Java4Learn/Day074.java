import java.applet.Applet; // from package only one class
import java.awt.Graphics;
//import javax.swing.Applet;
/*
<applet code="Helloworld" width="400" height="450">
*/
public class HelloWorld extends Applet
{
//declare a method as Paint 
@Override
    public void paint(Graphics g)
    {
      //draw a String (x,y) cordinates 
    g.drawString("Hello World!",30,30);
   } //End method paint
}
