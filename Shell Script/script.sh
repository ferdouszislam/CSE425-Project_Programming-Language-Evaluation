#!/bin/bash


################### helper functions start ###################

start=0
function startTimer()
{
    # start time
    start=`date +%s%N`    
}

function getRumtime()
{
    echo
    if [ $start == 0 ] 
    then
        runtime=-1
        echo "[ERROR: timer was not started]"
    else

        # end time
        end=`date +%s%N`
        #runtime in milliseconds
        runtime=$(((end-start)/1000000))
        echo "[task completed in $runtime ms]"
    fi

    echo
    start=0
    
}

function searchByDate()
{
    local date=$1 

    startTimer

    ## search file
    found=0
    while read -r line 
    do

        # split line by comma and put into columns array
        IFS=',' read -a columns <<<"$line"

        if [ ${columns[0]} = $date ] 
        then
            found=1
            echo
            echo "[search success!]"
            echo
            echo "New Confirmed = ${columns[1]}, Total Confirmed = ${columns[2]}"
            echo
            echo "New Deaths = ${columns[3]}, Total Deaths = ${columns[4]}"
            echo
            echo "New Recovered = ${columns[5]}, Total Recovered = ${columns[6]}"
            echo
            echo "New Tests = ${columns[7]}, Total Tests = ${columns[8]}"
            echo
            echo "Active Cases = ${columns[9]}"
            echo

            break 
        fi

    done < $mergedDatasetFile

    if [ $found == 0 ] 
    then
        echo
        echo "date not found"
    fi

    getRumtime
    
}

function searchByRange()
{

    echo

    startTimer
    
    local range=$1
    local searchColumn=$2

    declare -a resultArray

    if [[ $range = @(>)+([0-9]) ]] 
    then

        ## exclude the first character from $range
        range="${range:1}"

        ## search file
        lc=0
        while read -r line 
        do
            # skip the first line that contains column names
            if [[ $lc == 0 ]] 
            then
                lc=1
                continue
            fi

            # split line by comma and put into columns array
            IFS=',' read -a columns <<<"$line"

            if [[ ${columns[$searchColumn]} > $range ]] 
            then
                resultArray+=("${columns[0]}")
            fi

        done < $mergedDatasetFile

    elif [[ $range = @(<)+([0-9]) ]]
    then
        
        ## exclude the first character from $range
        range="${range:1}"

        ## search file
        lc=0
        while read -r line 
        do
            # skip the first line that contains column names
            if [[ $lc == 0 ]] 
            then
                lc=1
                continue
            fi

            # split line by comma and put into columns array
            IFS=',' read -a columns <<<"$line"

            if [[ ${columns[$searchColumn]} < $range ]] 
            then
                resultArray+=("${columns[0]}")
            fi

        done < $mergedDatasetFile

    elif [[ $range = +([0-9])@(-)+([0-9]) ]] 
    then
        # split the range
        IFS='-' read -a rs <<<"$range"

        ## search file
        lc=0
        while read -r line 
        do
            # skip the first line that contains column names
            if [[ $lc == 0 ]] 
            then
                lc=1
                continue
            fi

            # split line by comma and put into columns array
            IFS=',' read -a columns <<<"$line"

            if (( ${columns[$searchColumn]} >= ${rs[0]} & ${columns[$searchColumn]} <= ${rs[1]} )) 
            then
                resultArray+=("${columns[0]}")
            fi

        done < $mergedDatasetFile        

    else
        echo "invalid format."       
    fi

    searchResultFile="result.csv"
    >$searchResultFile

    ## print the unique elements of $resultArray
    resultArray=($(echo "${resultArray[@]}" | tr ' ' '\n' | sort -u | tr '\n' ' '))
    #echo ${resultArray[*]}
    local cnt=0
    for elem in "${resultArray[@]}"
    do
        ((cnt++))
        echo -n "$elem," >>$searchResultFile
        echo -n "$elem,"
    done

    ## check if any elemnent found or not
    if [[ $cnt == 0 ]] 
    then
        echo
        echo "no entry found."
    else
        echo
        echo
        echo "Total $cnt days matched the range (results saved into /result.csv file)"
    fi


    getRumtime
    
}

################### helper functions end ###################


# start of execution code
echo


################### merge files start ###################
mergedDatasetFile="data/merged/mergedDataSet.csv"

startTimer

echo "merging files..."
echo

# clear out the existing file
> $mergedDatasetFile
# write the common header to merged file
echo $(head -n 1 data/csvStructure.txt) > $mergedDatasetFile

# merge the files skipping the first line
tail -q -n +2 data/provided/*.csv >> $mergedDatasetFile

echo "merge complete!"
echo

getRumtime

echo -n "press return to continue"
read stopper
clear

################### merge files finish ###################



################### main ###################

while : 
do

clear

echo "################### Menu ###################"

## search options
echo
echo " 1. search by date"
echo " 2. search by daily new confirmed cases"
echo " 3. search by total confirmed cases"
echo " 4. search by daily new deaths"
echo " 5. search by total deaths"
echo " 6. search by daily new recovered"
echo " 7. search by total recovered"
echo " 8. search by daily new tests"
echo " 9. search by total tests"
echo "10. search by active cases"
echo
echo -n "select an option [1-10] > "
read input
echo

clear

## react to user input

if [ $input == 1 ]
then
# search by date
    echo -n "enter date [mm/dd/yyyy] > "
    read input

    ## check input format
    if [[ $input == +([0-9])@(/)+([0-9])@(/)+([0-9]) ]] 
    then
        searchByDate $input
    else
        echo "invalid input format."

    fi  

elif [[ $input != +([0-9]) || $input -gt 10 ]] 
then
# menu option input was wrong
    echo "invalid input format."

else
# search by a column

    echo
    echo "Valid input formats: [number1-number2], [>number1], [<number]"
    echo

    case $input in
        2)
            echo -n "enter new cases range - "
            read range
        ;;
        3) 
            echo -n "enter total cases range - "
            read range
        ;;
        4) 
            echo -n "enter new deaths range - "
            read range
        ;;
        5) 
            echo -n "enter total deaths range - "
            read range
        ;;
        6) 
            echo -n "enter new recovered range - "
            read range
        ;;
        7) 
            echo -n "enter total recovered range - "
            read range
        ;;
        8) 
            echo -n "enter new tests range - "
            read range
        ;;
        9) 
            echo -n "enter total tests range - "
            read range
        ;;
        10) 
            echo -n "enter active cases range - "
            read range
        ;;
        *) echo "invalid input."
        ;;
    esac

    searchByRange $range $input

fi

################### main ###################

echo
echo -n "Press [Ctrl+C] to exit, any other key to continue"
read stopper

done