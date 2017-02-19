#!/usr/bin/env bash

# Character for separating values
# (commas are not safe, because some servers return speeds with commas)
sep=";"
log=$PWD/alexa.csv

# Local functions
function str_extract() {
 pattern=$1
 # Extract
 res=`grep "$pattern" $log | sed "s/$pattern//g"`
 # Drop trailing ...
 res=`echo $res | sed 's/[.][.][.]//g'`
 # Trim
 res=`echo $res | sed 's/^ *//g' | sed 's/ *$//g'`
 echo $res
}

# Run Speedtest (NOTE: takes too long for Alexa, TODO use .cfg for Server-ID)
parentdir="$(dirname "$PWD")"
$parentdir/speedtest_cli/speedtest.py --share --secure --simple --server 5351 > $log

# Parse
from=`str_extract "Testing from "`
from_ip=`echo $from | sed 's/.*(//g' | sed 's/).*//g'`
from=`echo $from | sed 's/ (.*//g'`

server=`str_extract "Hosted by "`
server_ping=`echo $server | sed 's/.*: //g'`
server=`echo $server | sed 's/: .*//g'`
server_dist=`echo $server | sed 's/.*\\[//g' | sed 's/\\].*//g'`
server=`echo $server | sed 's/ \\[.*//g'`

if [ "$1" = "download" ]; then
  speed=`str_extract "Download: "`
elif [ "$1" = "upload" ]; then
  speed=`str_extract "Upload: "`
fi
# share_url=`str_extract "Share results: "`

# echo first number and the speed type (eg. Mbit/s)
# Read more about it the following commands here:
# - http://tecadmin.net/split-a-string-on-a-delimiter-in-bash-script/#
# - http://stackoverflow.com/a/17346794/1238150
IFS=’.’ read -ra result <<< "$speed"
declare -a 'a=('"$speed"')'
echo ${result[0]} ${a[1]}
