#include<stdio.h>
#include<conio.h>
#include<math.h>
float fun(float x)
{
return(x*x*x-4*x-9);
}
void bisection(float *x,float a,float b,int *itr)
{
*x=(a+b)/2;
++(*itr);
printf("iteration no. %3d X = %7.5f\n",*itr,*x);
}
int Bisection()
{
int itr=0,maxmitr;
float x,a,b,allerr,x1;
clrscr();
printf("enter the values of a,b, allowed error and maximum iteration\n");
scanf("%f%f%f%d",&a,&b,&allerr,&maxmitr);
bisection(&x,a,b,&itr);
do
{
if(fun(a)*fun(x)<0)
b=x;
else
a=x;
bisection(&x1,a,b,&itr);
if(fabs((double)x1-x)<(double)allerr)
{
printf("After %d iteration,root = %6.4f\n",itr,x1);
return 0;
}
x=x1;
}
while(itr < maxmitr);
printf("The solution does not converge or iteration are not sufficient");
return 1;
}