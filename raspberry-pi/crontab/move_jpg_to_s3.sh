#!/bin/bash
#
# Save diagnostic jpg files to s3
#

# Directory containing the JPG files
SOURCE_DIR="/tmp"

# S3 bucket name
S3_BUCKET="cat-doorbell-v2-jpg"

PATH="/usr/local/bin:${PATH}"

# Find .jpg files and move them to the specified S3 bucket
find $SOURCE_DIR -type f -name "*.jpg" | while read file; do
    aws s3 mv "${file}" s3://${S3_BUCKET}/ && echo "Moved ${file} to S3"
done
