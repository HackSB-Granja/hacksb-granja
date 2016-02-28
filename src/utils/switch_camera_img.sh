#!/bin/bash

symlink_path="../../data/images"

if [ "$(readlink -- "$symlink_path/last_camera_reading")" = $symlink_path/negative.jpg ]
then
    echo 'asdfasdf'
    ln -f -s $symlink_path/positive.jpg $symlink_path/last_camera_reading
else
    ln -f -s $symlink_path/negative.jpg $symlink_path/last_camera_reading
fi
echo "$(readlink -- "$symlink_path/last_camera_reading")"
