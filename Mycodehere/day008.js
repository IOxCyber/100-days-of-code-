#when you want to create more than one object of the same type.
#this isn't a variable , it's a keyword that hold the current obj value.
#new is keyword that use for creating the new object of the same type.


function person(name, age, color) {
  this.name = name;  
  this.age = age;
  this.color = color;
}

var obj1 = new person("Geon", 14, "blue");
var obj2 = new person("Rex", 20, "black");

document.write(obj1.age); # Outputs 14
document.write(obj2.name); # Outputs "Rex"
