#!/bin/bash
if [[ $(/usr/bin/id -u) -ne 0 ]]; then
    echo "Not running as root"
    exit
fi



DIR=$(dirname "$(readlink -f "$0")")
trap killgroup INT

killgroup(){
	echo killing...
	kill 0
}


python $DIR/cliControl.py & 
python $DIR/server.py &
wait

