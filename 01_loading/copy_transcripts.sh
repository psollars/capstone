#!/bin/bash

# ./umich/copy_transcripts.sh ./umich/2024-02\ SIADS\ 699 ~/Desktop/transcripts/siads-699 --ignore "*office-hour*"

if [ "$#" -lt 2 ]; then
  echo "Usage: $0 <source_directory> <destination_directory> --ignore <ignore_pattern>"
  exit 1
fi

SOURCE_DIR=$1
DEST_DIR=$2
IGNORE_PATTERN=""

if [ "$3" == "--ignore" ] && [ -n "$4" ]; then
  IGNORE_PATTERN=$4
fi

if [ ! -d "$SOURCE_DIR" ]; then
  echo "Source directory does not exist: $SOURCE_DIR"
  exit 1
fi

if [ ! -d "$DEST_DIR" ]; then
  echo "Destination directory does not exist, creating: $DEST_DIR"
  mkdir -p "$DEST_DIR"
fi

if [ -n "$IGNORE_PATTERN" ]; then
  find "$SOURCE_DIR" -type d -name "$IGNORE_PATTERN" -prune -o -type f -name "*.en.txt" -exec cp {} "$DEST_DIR" \;
else
  find "$SOURCE_DIR" -type f -name "*.en.txt" -exec cp {} "$DEST_DIR" \;
fi

echo "Copy complete."
