#!/bin/bash

DIR=$(dirname "$(readlink -f "$0")")
trap killgroup INT

killgroup(){
	echo killing...
	kill 0
}


python $DIR/cliControl.py & 
python $DIR/server.py &
wait

