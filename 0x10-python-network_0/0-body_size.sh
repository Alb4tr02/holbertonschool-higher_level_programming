#!/bin/bash
# script that takes in a URL, sends a request to that URL
curl -sI "$1" | awk '{if ($1 == "Content-Length:") print $2}'
