#!/usr/bin/env bash

OUTPUT_DIR=mint-wallpapers
TEMP_OUTPUT_DIR=/tmp/mint-wallpapers
BASE_URL=http://packages.linuxmint.com/pool/main/m

mkdir -p $OUTPUT_DIR
mkdir -p $TEMP_OUTPUT_DIR

PACKAGES=$(curl -s "$BASE_URL/" | grep -Eo 'mint-backgrounds[-a-zA-Z0-9]*' | uniq)
for package in $PACKAGES
do
    tar_gz_names=$(curl -s "$BASE_URL/$package/" | grep -Eo 'mint-backgrounds[-._a-zA-Z0-9]*\.tar\.gz' | uniq)
    for tar_gz in $tar_gz_names
    do
        echo "Downloading $BASE_URL/$package/$tar_gz..."
        curl -so "$TEMP_OUTPUT_DIR/$tar_gz" "$BASE_URL/$package/$tar_gz" && echo "OK." || echo "Failure."
    done
done

for tar_gz in "$TEMP_OUTPUT_DIR"/*.tar.gz
do 
    tar -xzf "$tar_gz" -C "$TEMP_OUTPUT_DIR"
done

for package in "$TEMP_OUTPUT_DIR"/*/
do
    find "$package" -type f \( -iname "*.jpg" -o -iname "*.jpeg" -o -iname "*.png" -o -iname "*.gif" -o -iname "*.bmp" -o -iname "*.tiff" -o -iname "*.webp" \) -exec cp {} "$OUTPUT_DIR" \;
done

rm -r $TEMP_OUTPUT_DIR

echo "Done"