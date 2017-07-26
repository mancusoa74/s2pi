#!/bin/bash

export FLASK_APP=s2pi.py
export FLASK_DEBUG=0

host=`ifconfig wlan0 | grep Bcast | cut -b 21-34`

flask  run --host=$host 2>&1 | grep -v poll


