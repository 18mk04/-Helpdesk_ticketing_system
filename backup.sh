#!/bin/bash

# Define database name and backup folder
DB_FILE="database.db"
BACKUP_FOLDER="backups"

# Create the backup folder if it doesn't exist
mkdir -p $BACKUP_FOLDER

# Create a timestamped backup
TIMESTAMP=$(date +"%Y%m%d_%H%M%S")
cp $DB_FILE $BACKUP_FOLDER/backup_$TIMESTAMP.db

echo "📦 Backup created: $BACKUP_FOLDER/backup_$TIMESTAMP.db"
