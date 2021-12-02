#!/bin/bash

alcf convert cl51 $1 temp.nc
alcf lidar cl31 temp.nc lidar/
alcf plot backscatter lidar/ plot/ cloud_mask: false sigma: 8
cp plot/*.png /tmp