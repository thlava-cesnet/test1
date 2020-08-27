#!/bin/bash

echo "scr1.sh"

DATE=$(date '+%y%m%d-%H%M%S')
echo ">$DATE<"
echo "$DATE" > tmp/date.txt

echo "Done."
