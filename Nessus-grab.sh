#!/bin/bash
#Quick and dirty script to grab finished Nessus scan reports and send via email
#Written to only grab reports that were run that same day this script is run
#Must have ssmtp and mpack installed and configured
#Place credentials to nessus server in file named login.txt in same directory as script
#Pass valid IP address of local nessus server and valid email address of report recipient as parameters: ./Nessus-grab.sh 192.168.1.1 boss@company.com
#Written by Jakx


input1=`echo $1 | grep -o "\."`
input2=`echo $2 | grep -o "\@"`

if [ -z "$1" ] || [ -z "$2" ] || [ "$1" = '-h' ] || [ "$1" = '--help' ] || [ -z "$input1" ] || [ -z "$input2" ]; then
        echo "Usage: ./Nessus-grab.sh [ip] [validemailaddress]"
        exit
fi

month=`date +%a\ %b\ %e`
username=`head -n 1 login.txt`
password=`tail -n 1 login.txt`
key=`wget --quiet --no-check-certificate --post-data "login=$username&password=$password" https://$1/login -O - | grep -o '[0-9a-z]\{48\}'`
wget --quiet --post-data "token=$key" --no-check-certificate https://$1/report/list -O - > reportlist.txt
cat reportlist.txt | grep -E "<name>|<readableName>|<timestamp>" | sed 's/></>\r\n</g' > reportlistclean.txt

cat reportlistclean.txt | while read line; do
        date=`echo $line | grep -o "[0-9]\{10\}<"`
        reportid=`echo $line | grep "</name>"`
        if [[ $reportid ]]; then
                reportnumber=`echo $reportid`
        fi
        if [[ $date ]]; then
                date2=`echo $date | sed 's/<//g'`
                realdate=`date -ud @$date2`
                today=`echo $line | sed 's/[0-9]\{10\}</'"$realdate"'</g' | grep "$month"`
                if [[ $today ]]; then
                        echo $reportnumber
                        echo $previousline
                        echo $today
                        cleanreportid=`echo $reportnumber | sed 's/<name>//g' | sed 's%</name>%%g'`
                        wget --quiet --post-data "report=$cleanreportid&chapters=vuln_by_plugin&format=html&token=$key" --no-check-certificate https://$1/chapter? -O - > test.html
                        sed "s%url=%url=https://$i%g" test.html > test2.html
                        url=`cat test2.html | grep "https" | sed 's%<title>Formatting the report</title><meta http-equiv="refresh" content="5;url=%%g' | sed 's/">//g'`
                        echo "generating report"
                        sleep 10
                        date=`date +%m%d%Y`
                        scantype=`echo $previousline | sed 's%<readableName>%%g' | sed 's%</readableName>%%g'`
                        echo $scantype
                        curl --silent --insecure --cookie "token=$key" $url > report_"$date"_"$scantype".html
                        todayclean=`echo $today | sed 's%<timestamp>%%g' | sed 's%</timestamp>%%g'`
                        mpack -s "Nessus report - $todayclean - $scantype" -o report_"$date"_"$scantype".txt report_"$date"_"$scantype".html
                        echo "emailing report_"$date"_"$scantype".txt"
                        cat report_"$date"_"$scantype".txt | /usr/sbin/ssmtp $2

                fi
        else
                previousline=$line
        fi
done

rm -f report_*
rm -f reportlist*
rm -f test*

