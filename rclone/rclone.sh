#!/bin/bash

folders=(Documentos faculdade Imagens)

echo "rclone run at $(date)" >> /home/daniel/.rclone.log
for folder in ${folders[@]}; do    
    rclone sync --verbose /home/daniel/"$folder" google-drive:rclone-desktop/"$folder"
done

