#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT
dbus-uuidgen > /var/lib/dbus/machine-id

#cd /root/SDA_ALL/48_firefox/

while true
do
	echo "NEW ..............."
	timeout 5m python3 48_ads.py
done
