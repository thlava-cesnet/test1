#!/bin/bash

echo "scr1.sh"

DATE=$(date '+%y%m%d-%H%M%S')
echo ">$DATE<"
echo "$DATE" | tee ./tmp/date.txt | tee ./test2/d1.txt > ./test2/d2.txt
ls -l ./tmp/date.txt
cat ./tmp/date.txt ./test2/d1.txt ./test2/d2.txt

echo "Done."
