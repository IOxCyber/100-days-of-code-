// program of fabonnaci series

var a=0,b=1,c=0;
n=prompt("enter the value of fabonaci");

for(var i=0;i<=n;i++)
{
    c=a+b;
    a=b;
    b=c;
document.write(c,"\n");
}

alert("You will found "+n+" digited fabonaci series");


//output
/* input 5
You will found 5 digited fabonaci series
1 2 3 5 8 13
