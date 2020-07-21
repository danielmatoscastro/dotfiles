#!/bin/bash

folders=("Documentos" "faculdade" "Imagens")

echo "rclone run at $(date)" >> "$HOME/.rclone.log"
for folder in ${folders[@]}; do    
    rclone sync --verbose "$HOME/$folder" "google-drive:rclone-desktop/$folder"
done

