#!/bin/bash

rclone move /tmp/ google-drive-cloning:/CatDoorbellV3/rpi-captured-files/wav/meow --include "/meow*.wav" --verbose

rclone move /tmp/ google-drive-cloning:/CatDoorbellV3/rpi-captured-files/wav/unknown --include "/unknown*.wav" --verbose

rclone move /tmp/ google-drive-cloning:/CatDoorbellV3/rpi-captured-files/jpg --include "/*.jpg" --verbose
