#!/bin/sh

sensors | grep Tctl | awk '{print substr($3, 2, length($3)-5)}' | tr "\\n" " " | sed 's/ /°C  /g' | sed 's/  $//'
