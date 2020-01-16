#!/bin/bash
#Follow redirections
curl -sI "$1" | grep Allow | cut -d$' ' -f2-
