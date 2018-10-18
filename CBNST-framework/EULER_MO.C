#include<stdio.h>
#include<math.h>
#include<conio.h>
#define F(x,y) (x-y)/(x+y)
void main()
{
int i,n,Itrsn;
float x[5],y[50],yc[50],h,yp,p,xn;
clrscr();
printf("\n Enter the values: x[1],y[1],h,xn:\n");
scanf("%f%f%f%f",&x[1],&y[1],&h,&xn);
yp=y[1]+h*F(x[1],y[1]);
Itrsn=(xn-x[1])/h;
printf("\n\n X=%f y=%f\n",x[1],y[1]);
for(i=1;i<=Itrsn;i++)
{
x[i+1]=x[i]+h;
for(n=1;n<=50;n++)
{
yc[n+1]=y[i]+(h/2.0)*(F(x[i],y[i])+F(x[i+1],yp));
printf("\nN=%d y=%f",n,yc[n+1]);
p=yc[n+1]-yp;
if(fabs (p)<0.0001)
goto NEXT;
else
yp=yc[n+1];
}
NEXT:
y[i+1]=yc[n+1];
printf("\n\n X=%f Y=%f\n",x[i+1],yp);
}
getch();
return;
}



/*
:::NOTATION USED IN THE PROGRAM:::

 x(1) is an array of the initial value of x.
 y(1) is an array of the initial value of y.
 h is the spacing value of x.
 Xn is the last value of x at which value of y is required.

 :::TEST FOR:::
 x[1]=0
 y[1]=1
 h=0.02
 Xn=0.06
*/
