#!/bin/bash

file1=$1
file2=$2
output_file="output.txt"

while read line1 && read line2 <&3; do
    echo "$line1" >> "$output_file"
    echo "$line2" >> "$output_file"
done < "$file1" 3< "$file2"

