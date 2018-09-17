/*"Methods" are "functions" that are stored as object "properties". 
and referenced using the "this" keyword that is used as a reference to the current object,
meaning that you can access the objects properties and methods using it.
*/
//adding the methods

function person(name, age) {
    this.name = name;  
    this.age = age;
    this.changeage = function(age) {
      this.age = age;  
    }
    this.changeName = function (name) {
        this.name = name;
    }
}

var p = new person("David", 21);
var x = changeName="John";
document.write(x+"<br>"); 
document.write(changeAge=23);
document.write("<br>"+p.name,"<br>"+p.age); 

/*
OUTPUT
John
23
David
21

explanation : we have defined a method named changeName for our person, which is a function, 
that takes a parameter name and assigns it to the name property of the object. 
this.name refers to the name property of the object. */
