#!/bin/bash
# usage: ./size.bash file1 file2 ...
# echo file_size & file_name

echo "Size File"

for f in $*
do
	wc -c $f
done
	
