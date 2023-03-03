#!/bin/bash

# Set the URL of the online word list
url="https://raw.githubusercontent.com/dwyl/english-words/master/words.txt"

# Download the word list and save it to a file
curl -o words.txt "$url"