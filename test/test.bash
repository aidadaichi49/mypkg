#!/bin/bash
# SPDX-FileCopyrightText: 2025 Daichi Aida <da1649ichi@gmail.com>
# SPDX-License-Identifier: BSD-3-Clause

dir=~
[ "$1" != "" ] && dir="$1"

cd $dir/ros2_ws

colcon build

source $dir/.bashrc

echo "hello" | timeout 10 ros2 run mypkg keyboard_talker > output.txt 2>&1

grep 'hello' output.txt
