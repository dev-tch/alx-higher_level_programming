#!/bin/bash
# display only body of status code 200
[ "$(curl -sL -w "%{http_code}" "$1" | tail -c 3)" -eq 200 ] && curl -sL "$1"
