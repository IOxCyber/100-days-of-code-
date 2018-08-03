function done() {
            var n = confirm("enjoyed this example?"); 
                    if (n === true) {
                        alert("thanks!");
                    }
                    else {
                        alert("feel free to make any suggestions!");
                    }
        }


    function mainfn() {
  var x = prompt("What type of pop-up box is this? prompt, alert, or confirm?");
  /* alert(x); // this is temporary to help in de-bugging. */                            
  if (x == "prompt") {
                               alert("correct!");
                    }
          else if (x === null){
          return; 
          
           //this is to allow you to press cancel to exit the dialog, remove it and see what happens if you'd like.
                            }
            else {
       alert("wrong");
    var y = confirm("try again?");
     if (y === true) {
                                        mainfn();  // to give another try
                                    } 
      else {
                                        return; //to exit the dialog box
                                    }                            
                            }
                    }
                    
  function alrt() {    
            alert("this is an alert box")
        }                 
        
        
        
                    
