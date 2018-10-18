	#include<stdio.h>
	#include<conio.h>
	#include<EULER.h>
	#include<EULERM.h>
	#include<RUNGE.h>
	#include<BISECT.h>
	#include<NEWTON.h>
	#include<Error.h>
	#include<Picard.h>
	#include<math.h>

	CBNST()
	{
	int choice;
	char x;
	clrscr();
	printf("\t\t :*:*: WELCOME TO THE CBNST FRAMEWORK :*:*:\n\n");

	do{
	printf("\t\t Enter Your Choice \n\n \t\t 1 for Euler Method \n\t\t 2 for Euler Modified Method \n\t\t 3 for Runge Kutta Method\n\t\t 4 for Bisection Method\n\t\t 5 for Newton Method\n\t\t 6 for Calculate Error\n\t\t 7 for Picard Method\n\t\t:");
	scanf("%d",&choice);
	switch(choice)
	{
	case 1:
	printf("\t\t :*: Euler Method Called :*:\n");
	Euler();
	break;

	case 2:
	printf("\t\t :*: Euler Modified Method Called :*:\n");
	EulerM();
	break;

	case 3:
	printf("\t\t :*: Runge Kutta Method Called :*:\n");
	Runge();
	break;

	case 4:
	printf("\t\t :*: Bisection Method Called :*:\n");
	Bisection();
	break;

	case 5:
	printf("\t\t :*: Newton Raphson Method Called :*:\n");
	Newton();
	break;

	case 6:
	printf("\t\t :*: Calculate the Error :*:\n");
	Error();
	break;

	case 7:
	printf("\t\t :*: Picard Method :*:\n");
	Picard();
	break;

	}
	printf("\n\n\t\t :*: Do You Want More Methods To Use....Press y/n ? :*:\n");
	x=getch();
	}while(x=='y');
	getch();
	return ;
	}
