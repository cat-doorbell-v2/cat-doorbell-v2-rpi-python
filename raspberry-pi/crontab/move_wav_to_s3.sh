#!/bin/bash

# Target S3 bucket name
BUCKET_NAME="cat-doorbell-v3-samples"

# Source directory for .wav files
SOURCE_DIR="/tmp"

# Find and move .wav files to the S3 bucket
find "${SOURCE_DIR}" -type f -name "*.wav" -exec aws s3 mv {} s3://${BUCKET_NAME}/ \;
