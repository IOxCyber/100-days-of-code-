var person = {
    name: "John",
     age: 31, 
    favColor: "green",
     height: 183
};


var x = person.age; 
var y = person['age']+1;//add 1 to value of x.

if(x==y)
document.write(x);
else
document.write(y);

/* you can access Object's property by two manner.
1.Just ObjectName.property;
2.Or use ObjectName[property];



