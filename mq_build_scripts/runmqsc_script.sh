#!/bin/bash
box=$1
port=$2
script=$3
source /opt/mqm/bin/setmqenv -s
echo MQSERVER='SYSTEM.RF.SVRCONN/TCP/'$box'('$port')'
export MQSERVER='SYSTEM.RF.SVRCONN/TCP/'$box'('$port')'
#echo $script | runmqsc -c
runmqsc -c  < $script
