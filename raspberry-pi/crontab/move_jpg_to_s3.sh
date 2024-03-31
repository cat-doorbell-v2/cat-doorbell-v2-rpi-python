#!/bin/bash
#
# Save diagnostic jpg files to s3
#

# Directory containing the JPG files
SOURCE_DIR="/tmp"

# S3 bucket name
S3_BUCKET="cat-doorbell-v2-jpg"

PATH="/usr/local/bin:${PATH}"

find "${SOURCE_DIR}" -type f -name "*.jpg" -exec aws s3 mv {} s3://${S3_BUCKET}/ \;
