#!/bin/bash

folders=(Documentos faculdade Imagens)

for folder in ${folders[@]}; do    
    rclone sync --verbose /home/daniel/"$folder" google-drive:rclone-desktop/"$folder"
done

