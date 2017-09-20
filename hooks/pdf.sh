#!/bin/bash

# requires electron-pdf
# 	https://github.com/fraserxu/electron-pdf
# 	npm install electron-pdf -g

# requires exiftool
# 	brew install exiftool


SOURCE="${BASH_SOURCE[0]}"
while [ -h "$SOURCE" ]; do # resolve $SOURCE until the file is no longer a symlink
  DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
  SOURCE="$(readlink "$SOURCE")"
  [[ $SOURCE != /* ]] && SOURCE="$DIR/$SOURCE" # if $SOURCE was a relative symlink, we need to resolve it relative to the path where the symlink file was located
done
DIR="$( cd -P "$( dirname "$SOURCE" )" && pwd )"
DIR=$(dirname ${DIR})

IN="index.html"
OUT="paul_crane.pdf"

electron-pdf -m 0 ${DIR}/${IN} ${DIR}/${OUT}
exiftool -Author="Paul Crane" -Title="Dr." "${OUT}"
