#!/bin/bash
 
# Path to your Python script

PYTHON_SCRIPT="/home/sharukh/CIAP/one.py"
 
# SSID of the home network

HOME_SSID="AEPL-R&D"
 
# Check the current SSID
while true; do
    CURRENT_SSID=$(iwgetid -r)

    if [ "$CURRENT_SSID" == "$HOME_SSID" ]; then
	echo "Connected to $HOME_SSID. Running the python script."
        python3 "$PYTHON_SCRIPT"
	break
    else
	echo "Not connected to $HOME_SSID. Retrying in 10 Seconds...."
    fi

    sleep 10

done


 
