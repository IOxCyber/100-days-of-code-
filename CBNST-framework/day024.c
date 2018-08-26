//save it as .h

void  add()
    {
        int a[10] = {1,2,3,4,5,6,7,8,9,10};
        int i,add=0;
        printf("\t\t ARRAY FUNCTION CALLED.\n\n");
        for(i=0;i<10;i++)
        add=add+a[i];
        printf("\t The Addition of Array=%d",add);
        
    }
    
    
    //save this module as .h
void sum()
{
	int a, b, sum;
	a=12,b=21;
/*
	printf("Enter the value of a & b\n\n");
	scanf("%d %d",&a,&b);	
*/
printf("\t\t::SUM FUNCTION CALLED::\n\n");
	sum=a+b;
	printf("%d",sum);
	//save this as .h in the same or hearder file folder.
}
    
    
    //save it as .c

#include<stdio.h>
#include<conio.h>
#include<test1.h>
#include<test2.h>
void main()
{
	sum();
	printf("\n\n");
	add();
	getch();
}
    
    
    
