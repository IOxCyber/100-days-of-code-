<?php
    echo "Filename of current exe. <b>script</b>: ".$_SERVER['PHP_SELF']."<br>";
    echo "IP address of host server: ".$_SERVER['SERVER_ADDR']."<br>";
    echo "Name of host server: ".$_SERVER['SERVER_NAME']."<br>";
    echo "The server machine's port: ".$_SERVER['SERVER_PORT']."<br>";
    echo "Ip address of user's side:".$_SERVER['REMOTE_ADDR']."<br>";
    echo "Port used on user's machine to communiate with web server: ".$_SERVER['REMOTE_PORT']."<br>";
    echo "Pathway of current exe. script".$_SERVER['SCRIPT_FILENAME']."<br>";
    echo "Path of current script".$_SERVER['SCRIPT_NAME']."<br>";
    

// NOTE:: Run the code on your machine not on online compiler.If you run on online compiler then it'll show error. 
?>
