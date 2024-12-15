# Read from the file file.txt and output the tenth line to stdout.
input="file.txt"
m=10
counter=1
while IFS= read -r line
do
    if [ $counter -eq $m ]
    then
        echo "$line"
        break
    else
        ((counter++))
    fi
done < "$input"