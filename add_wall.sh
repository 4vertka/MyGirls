#!/bin/bash

# Set the path to the images folder
image_folder="./walls"

# Create the markdown content for each image in the folder
for img in $image_folder/*; do
  echo "![$(basename "$img")]($img)" >>README.md
done
