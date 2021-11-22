#!/bin/bash

alcf convert cl51 $1 /tmp/test.nc
alcf auto lidar cl51 /tmp/test.nc /tmp/
cp /tmp/plot/backscatter/*.png $2