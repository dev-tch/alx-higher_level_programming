#!/bin/bash
# display only body of status code 200
[ "$(curl -s -w "%{http_code}" "$1" | tail -c 3)" -eq 200 ] && curl -s "$1"
