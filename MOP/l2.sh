#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT

dbus-uuidgen > /var/lib/dbus/machine-id

while true
do
	echo "NEW ..............."
	timeout 3m python3 chom.py
done
