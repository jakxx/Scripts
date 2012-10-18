#!/bin/sh
#Script to grab a website's robots.txt file and open all "disallow" entries in a web browser


input1=`echo $1 | grep -o "\."`


if [ -z "$1" ] || [ "$1" = '-h' ] || [ "$1" = '--help' ] || [ -z "$input1" ]; then
echo "Usage: ./robocop.sh [www.targetsite.com]"
        exit
fi

curl "$1/robots.txt" > robots.txt

firefox -net-tab `cat robots.txt | sed "s%Disallow: /%http://$1/%g" | grep http`
