	#include<stdio.h>
	#include<conio.h>
	#include<EULER.h>
	#include<EULERM.h>
	#include<RUNGE.h>

	void main()
	{
	int choice;
	char x;
	clrscr();
	printf("\t\t :*:*: WELCOME TO THE CBNST FRAMEWORK :*:*:\n\n");

	do{
	printf("\t\t Enter Your Choice \n\n \t\t 1 for Euler Method \n\t\t 2 for Euler Modified Method \n\t\t 3 for Runge Kutta Method\n");
	scanf("%d",&choice);
	switch(choice)
	{
	case 1:
	printf("\t\t :*: Euler Method Called :*:\n");
	Euler();
	break;

	case 2:
	printf("\t\t :*: Euler Modified Called :*:\n");
	EulerM();
	break;

	case 3:
	printf("\t\t :*: Runge Kutta Called :*:\n");
	Runge();
	break;
	}
	printf("\n\n\t\t :*: Do You Want More Methods To Use ? :*:\n");
	x=getch();
	/*printf("\t\t :*: Milne Method Called :*:\n");
	Milne();*/
	}while(x=='y');
	getch();

	}
