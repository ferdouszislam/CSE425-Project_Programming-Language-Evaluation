#!/bin/bash

# start time
start=`date +%s%N`
# end time
end=`date +%s%N`
#runtime in milliseconds
runtime=$(((end-start)/1000000))


## input format checking
echo -n ">"
read input

if [[ $input = @(>)+([0-9]) ]] 
then
    echo "greater than format"

elif [[ $input = @(<)+([0-9]) ]]
then
    echo "less than format"

elif [[ $input = +([0-9])@(-)+([0-9]) ]] 
then
    echo "range specified"

else
    echo "invalid format!"       
fi


## function example

echo -n ">"
read input

function foo()
{
    local arg=$1

    if [[ $arg == "" ]] 
    then
        return 0
    fi

    # functions can only return numbers 0-255
    local str="$arg added"
    echo $str

    return 1
}

foo $input
var=$?

echo "function returned " $var

## variables
input=$((5+input))
let "input*=2"
echo $input


# # clears out file
# > $tmp1
# # appends lines to file
# echo "column1, column2" >> $tmp1
# echo "hello, there" >> $tmp1
# echo "world, people" >> $tmp1

# # echo
# # cat $tmp1

# > $tmp2
# echo "column1, column2" >> $tmp2
# # array of strings
# declare -a writeLines
# writeLines+=("bye, world")
# writeLines+=("world, monsters")
# # write the whole array to file, each elements in separate lines
# printf "%s\n" "${writeLines[@]}" >> $tmp2

# # echo
# # cat $tmp2

# # read lines(except first one) from tmp1.txt, tmp2.txt and merge into mergedTemp.txt

# > $mergedTmp
# echo "column1, column2" >> $mergedTmp

# n=0

# # read from tmp1.txt and write to mergedTmp.txt
# while read -r line 
# do

#     if [ $n -ne 0 ] 
#     then
#         echo "$line" >> $mergedTmp  
#     fi

#     ((n++))

# done < $tmp1

# n=0

# # read from tmp2.txt and write to mergedTmp.txt
# while read -r line 
# do

#     if [ $n -ne 0 ] 
#     then
#         echo "$line" >> $mergedTmp  
#     fi

#     ((n++))

# done < $tmp2

# cat $mergedTmp


# echo