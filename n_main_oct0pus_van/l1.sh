#!/usr/bin/env bash
clear
trap "echo oh;exit" SIGTERM SIGINT

cd /root/SDA_ALL/48_firefox/

while true
do
	echo "NEW ..............."
	python3 google_let.py
done
