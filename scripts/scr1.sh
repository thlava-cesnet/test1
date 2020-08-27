#!/bin/bash

echo "scr1.sh"

DATE=$(date '+%y%m%d-%H%M%S')
echo ">$DATE<"
echo "$DATE" | tee ./tmp/date.txt | tee ./d1.txt > ./d2.txt
ls -l ./tmp/date.txt
cat ./tmp/date.txt ./d1.txt ./d2.txt

echo "Done."
