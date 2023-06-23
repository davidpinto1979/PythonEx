# Using Python to Interact with the Operating System/Week-6
# Qwiklabs Assessment: Editing Files Using Substrings 

#!/bin/bash

> oldFiles.txt

files=$(grep " jane " ../data/list.txt | cut -d ' ' -f 3);

for file in $files; do
    if test -e "..${file}"; then echo "..${file}" >> oldFiles.txt; fi
done