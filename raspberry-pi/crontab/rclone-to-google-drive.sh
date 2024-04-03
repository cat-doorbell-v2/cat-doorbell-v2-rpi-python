#!/bin/bash

rclone move /tmp/ google-drive-cloning:/CatDoorbellV3/rpi-captured-files/wav --include "/*.wav" --verbose

rclone move /tmp/ google-drive-cloning:/CatDoorbellV3/rpi-captured-files/jpg --include "/*.jpg" --verbose
