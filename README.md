# ALCF docker

Containerized Automatic Lidar and Ceilometer Processing Framework (ALCF) 1.1.0. For more information, check https://github.com/alcf-lidar/alcf. 

[TOC]

## Prerequisite

+ Docker
+ Python
  + boto3, docker, fr_helpers
+ MS share mounted

## Build docker image

```bash
docker build . --tag alcf:1.1.0
```

## Run ALCF

```python
python main.py -sid NZNPA -dt 2021-11-22
```

The results can be found in */tmp/lidar*, */tmp/plot*, and */tmp/stats* folder. The backscatter plot also can be found in the given s3 place.

Note that the following CONST will need to be updated according to the system settings:

**MS_SHARE_FOLDER** - MetService share stores the real-time ceilometer backscatter data (e.g., `/mnt/storm/Ops_Data/Ceilometer_Backscatter_Data/Wellington_Forecast_Centre`).

**S3_ARCHIVE_FOLDER** - S3 folder to archive the results (e.g., `s3://metservice-research-us-west-2/research/experiments/yizhe/ceilometers`).

**profile_name** - AWS profile name (e.g., `research-normaluser`).

## Supported ceilometer sites

The following sites are available for getting ceilometer data.

| Name  | Notes |
| ----- | ----- |
| NZAAA |       |
| NZAPA |       |
| NZCHA |       |
| NZDNA |       |
| NZGSA |       |
| NZHNA |       |
| NZNPA |       |
| NZNRA |       |
| NZOHA |       |
| NZQHA |       |
| NZROA |       |
| NZTGA |       |
| NZWKA |       |
| NZWNA |       |
| NZWRA |       |

