function varTest() {
    var x = 1;
    if (true) {
        var x = 2;  // same variable, here u just update the var value.
        document.write(x+"<br>");  
    }
    document.write(x);  
}

function letTest() {
    let x = 1; // accessable through out the function.
    if (true) {
        let x = 2;  // different variable, scope only in if statement.
        document.write("<br>"+x+"<br>");  
    }
    document.write(x);  
}

varTest();
letTest();


/*Output

2
2
2
1 
*/
