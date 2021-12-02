# ALCF container

Containerized Automatic Lidar and Ceilometer Processing Framework (ALCF) latest version (1.1.2). For more information, check https://github.com/alcf-lidar/alcf.

[TOC]

## Prerequisite

- Docker
- Python
  - boto3, docker, fr_helpers
- MS share mounted

## Build docker image

```bash
docker build . --tag alcf:1.1.2
```

## Run ALCF

```python
python main.py -sid NZNPA -dt 2021-11-22
```

The result image can be found in both _/tmp_ and _/home/yzhan/ceilometer_ folders.

Note that the following CONST will need to be updated according to the system settings:

**MS_SHARE_FOLDER** - MetService share stores the real-time ceilometer backscatter data (e.g., `/mnt/storm/Ops_Data/Ceilometer_Backscatter_Data/Wellington_Forecast_Centre`).

**S3_ARCHIVE_FOLDER** - S3 folder to archive the results (e.g., `s3://metservice-research-us-west-2/research/experiments/yizhe/ceilometers`).

**profile_name** - AWS profile name (e.g., `research-normaluser`).

## Supported ceilometer sites

The following 16 sites are available for getting ceilometer data.

| Name  | Notes             |
| ----- | ----------------- |
| NZAAA | Auckland Aero A   |
| NZAPA | Taupo Aero        |
| NZCHA | Christchurch Aero |
| NZDNA | Dunedin Aero      |
| NZGSA | Gisborne Aero     |
| NZHNA | Hamilton Aero     |
| NZNPA | New Plymouth Aero |
| NZNRA | Napier Aero       |
| NZNVA | Invercargill Aero |
| NZOHA | Ohakea Aero       |
| NZQNA | Queenstown Aero   |
| NZROA | Rotorua Aero      |
| NZTGA | Tauranga Aero     |
| NZWKA | Whakatane Aero    |
| NZWNA | Wellington Aero A |
| NZWRA | Whangarei Aero    |

## Remove noises

The noises in the original backscattering plot is removed by specifying the σ in the plot function to 8.
