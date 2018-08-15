//1. Method I  
var courses = new Array("HTML", "CSS", "JS"); 
document.write("--1st output--<br><br>"+courses[0]);

document.write("<br>"+courses[10]+"<br>"); //access the out of index value.

courses[0]="Python";
document.write(courses[0]+"<br><br> --2nd output-- <br><br>");     


/*
An array is a special type of object.
An array uses numbers to access its elements, and an object uses names to access its members.
*/
//2. Method II

var courses = Array();

 courses[0]=("HTML");
 courses[1]=("CSS");
 courses[2]=("JS"); 

document.write(courses[0]+"<br><br> --3rd output-- <br><br>");

/*
JavaScript arrays are dynamic,
so declare an array and not pass any arguments with the "Array()" constructor. 
then add the elements dynamically.
*/

//3. Method III

var courses = ["hi","hello","GoodDay"];
document.write(courses[2]);

/* Output

HTML
undefined
Python

--2nd output-- 

HTML

--3rd output-- 

GoodDay
*/
