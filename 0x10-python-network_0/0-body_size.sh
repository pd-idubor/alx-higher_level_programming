#!/bin/bash
#Display body size of response
curl -sI "$1" | grep Content-Length | cut -d: -f2 | tr -d " "
