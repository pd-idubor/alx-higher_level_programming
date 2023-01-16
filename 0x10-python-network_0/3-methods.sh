#!/bin/bash
#Displays all acceptable HTTP methods
curl -sI $1 | grep Allow | cut -c 8-
