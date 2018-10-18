# include<stdio.h>

 void main()

 {
      float fxy(float x,float y),x0,y0,x1,y1,xn,h,k1,k2;

      int ns,i;

      printf("\nEnter x0,xn,ns,y0:");

      scanf("%f %f %i %f",&x0,&xn,&ns,&y0);

      h=(xn-x0)/ns;

      for(i=0;i<=ns;i++)

      {

           printf("\n%f %f",x0,y0);

           k1=h*fxy(x0,y0);

           y1=y0+k1;

           x1=x0+h;

           k2=h*fxy(x1,y1);

           y1=y0+(k1+k2)/2;

           y0=y1;

           x0=x1;

      }

 }

 float fxy(float x,float y)

 {
      int xy;

      float dy=(x+y)/(y*y-sqrt(xy));

      return dy;

 }