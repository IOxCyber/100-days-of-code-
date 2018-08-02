echo "Enter the Number"
read NUM
if [ `expr $NUM % 2` -eq 0 ]
then
echo "Number is Even"
else
echo "Number is Odd"
fi

# No need to terminate using semi colon(;) like c,c++ etc. 
# We use echo to print message on the screen 
# We use read to scan a number from user
# if condition will be write using the keyword "expr"
# -eq means equal to
# Here always use the if as if,then,statement,else,fi / fi to end if condition 
