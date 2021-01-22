#!/usr/bin/env bash

# BACKUP_IGNORE_FILE=".backupignore"
# TIMESHIFT_FOLDER_SRC="/home/daniel/data/timeshift"
# TIMESHIFT_FOLDER_DST="/media/daniel/hd-externo-ext4"
# REGULAR_BACKUP_FOLDER_SRC="/home/daniel/data"
# REGULAR_BACKUP_FOLDER_DST="/media/daniel/hd-externo"
# REPOS_FOLDER="/home/daniel/data/meus-repositorios"

BACKUP_IGNORE_FILE=".backupignore"
TIMESHIFT_FOLDER_SRC="/home/daniel/data/timeshift"
TIMESHIFT_FOLDER_DST="/media/daniel/hd-externo-ext4"
REGULAR_BACKUP_FOLDER_SRC="/home/daniel/data"
REGULAR_BACKUP_FOLDER_DST="/media/daniel/hd-externo"
REPOS_FOLDER="/home/daniel/data/meus-repositorios"

for folder in $REGULAR_BACKUP_FOLDER_SRC/*
do
    if ! grep -q "$folder" "$BACKUP_IGNORE_FILE";
    then  
        echo "$folder"
    fi
done