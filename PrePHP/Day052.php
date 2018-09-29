//CODE@1
<?php
//A multidimensional array contains one or more arrays.
//Dimension of array indicates the no. of indices you would  need to select an elem.
$games=array('0'=>array('player','unknown'),'1'=>array('battle','ground'),'2'=>array('pubg','game'));

print_r($games);
//or
echo "<br>";
echo $games['2'][1];
echo $games['2'][0];

/*
$n=count($games);
for($i=0;$i<$n;$i++)
{
for($j=0;$j<=$n;$j++)
{ 
    if($j>=2)
    break;
    else{   
echo ($games[$i][$j]);
echo "<br>";
}}}*/
?>

//CODE@2
<?php
/*Associative Arrays
Associative arrays are arrays that use keys that you assign  to them.
or in other words we assign value to by using key in associative array but in numeric we assign by the Index.*/
$jio=array("Eastside"=>"30","YoungBlood"=>"50");
echo $jio['Eastside']+$jio['YoungBlood'];  
//You can't assign a string to array's key as a value.
echo "<br>";

//Another way 
$jio['In']="1";
$jio['My']="2";
$jio['Feelings']="3";
echo $jio['In'];
echo "<br>";
echo $jio['My'];
echo "<br>";
echo $jio['Feelings'];
echo "<br>";

//afterall entire array shown here.
print_r($jio);
?> 

CODE@3
<?php
//Numeric or Index Array
//NUmeric or Indexed Arrays associate a numeric Index with thier value.
$a[0]="I'm";
$b[1]="Not";
$c[2]="Alone";
echo "I Believe That <b>$a[0]</b> $b[1] <strong>$c[2]!</strong>";

//other way to Create Numeric Array with "Array" Keyword
$song=array("Battle","Synphony",1);
echo "<br>I <b>love</b> the song <b>$song[0] $song[1]</b> and It's No. $song[2] Song.";

//Another Way to Create Array
$jio=["The","Night",'V',"Met"];
echo "<br>Another Best Song is <b>$jio[0] $jio[1] $jio[2] $jio[3].</b>"

?>
