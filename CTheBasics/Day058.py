
#include<stdio.h>
#include<string.h>
int main()
{
  int x;
  char c;
  char city[40];
  do{
  printf("\t\n Enter String Input Output type \n scanf,printf @1\ngets,puts @2\nfgets,fputs @3\n");
  scanf("%d",&x);
  switch(x)
  {
  case 1:
  printf("\n Enter Your City Name");
  scanf("%s",city);
  printf("%s",city);
  break;

  case 2:
  printf("\n Enter Your city Name");
  gets(city);
  puts(city);
  break;

  case 3:
  printf("\n Enter Your city Name");
  fgets(city,40,stdin);
  fputs(city,stdout);
  break;
  }
  printf("\nDo you want to Continue??");
  scanf("%c",c);
  }while(c=='y');

  return 0;
}
