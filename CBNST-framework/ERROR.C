#include<stdio.h>
#include<conio.h>
#include<math.h>
void main()
{
float true_val,approx_val,absolute_err,relative_err,percentage_err;
clrscr();
printf("\n You Are On Calculating Error \n");
printf("Enter the value of true value and approximate value \n");
scanf("%f%f",&true_val,&approx_val);
absolute_err=(true_val-approx_val);
relative_err=absolute_err/true_val;
percentage_err=relative_err*100;
printf("The absolute error is %f\n",absolute_err);
printf("The relative error is %f\n",relative_err);
printf("The percentage error is %f\n",percentage_err);
getch();
}