#!/bin/bash
# print header Content-Length value
curl -sI "$1" | grep -i "Content-Length" | awk -F ': ' '{print $2}'
