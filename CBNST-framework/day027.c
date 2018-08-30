                                            /* Euler Method */

#include<stdio.h>
#include<conio.h>
#define F(x,y) (x-y)/(x+y)
void main()
{
int i,n;
float x0,y0,h,xn,x,y;
printf("\n Enter the values: x0,y0,h,xn: \n");
scanf("%f%f%f%f",&x0,&y0,&h,&xn);
n=(xn-x0)/h+1;
for(i=1;i<=n;i++)
{
y=y0+h*F(x0,y0);
x=x0+h;
printf("\n X=%f Y=%f",x0,y0);
if(x<xn)
{
x0=x;
y0=y;
}}
//return;
getch();
}
/*
      ::NOTATIONS USED IN THE PROGRAM::
X0 is the initial value of x.
y0 is the initial value of y.
h is the spacing value of x.
Xn is the last value of x where value of y is required.
*/
