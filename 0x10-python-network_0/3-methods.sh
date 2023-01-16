#!/bin/bash
#Displays all acceptable HTTP methods
curl -sX "OPTIONS" $1
