"""
1. Copy the ceilometer raw file from MS's share to local /tmp folder.
2. Mount local /tmp folder on ALCF container's /tmp folder and run ALCF.
3. (optional) Save outputs on s3.
"""

from argparse import ArgumentParser
from datetime import datetime
from fr_helpers import aws
import os
import shutil
import boto3
import docker

boto3.setup_default_session(profile_name="research-normaluser")
S3_RESOURCE = boto3.resource("s3")
client = docker.from_env()


MS_SHARE_FOLDER = (
    "/mnt/storm/Ops_Data/Ceilometer_Backscatter_Data/Wellington_Forecast_Centre"
)
LOCAL_TEMP_FOLDER = "/tmp"
LOCAL_ARCHIVE_FOLDER = "/home/yzhan/ceilometer"
S3_ARCHIVE_FOLDER = (
    "s3://metservice-research-us-west-2/research/experiments/yizhe/ceilometers"
)


def copy_ceilometer_data(sid: str, dt: datetime):
    """Copy the ceilometer raw file from MS's share to local.

    Args:
        sid (str): station ID
        dt (datetime): datetime of ceilometer data
    """
    raw_file = f"{sid}/A1{dt:%m%d}00.DAT"
    raw_file_path = os.path.join(MS_SHARE_FOLDER, raw_file)
    if os.path.exists(raw_file_path) == False:
        print(f"Cannot find ceilometer data at datetime {dt:%m%d} at station {sid}")
        exit(1)

    dst_file = os.path.join(LOCAL_TEMP_FOLDER, f"{sid}_{dt:%Y-%m-%d}.DAT")
    shutil.copy(raw_file_path, dst_file)

    return dst_file


def archive_data_on_s3(sid: str, data_path: str):
    """Save data on s3.

    Args:
        sid (str): station ID, used to separate subfolders
        data_path (str): path of data to be saved
    """
    s3_folder = os.path.join(S3_ARCHIVE_FOLDER, sid)
    aws.s3.copy(data_path, s3_folder, S3_RESOURCE)
    os.remove(data_path)


def run_alcf(sid: str, dt: datetime):
    """Run ALCF and save the output.

    Args:
        sid (str): station ID
        dt (datetime): datetime of ceilometer data
    """
    ceilometer_data = copy_ceilometer_data(sid, dt)

    client.containers.run(
        image="alcf:1.1.0",
        command=f"{ceilometer_data} /tmp",
        volumes=[
            "/tmp:/tmp",
        ],
    )

    img_raw = os.path.join(LOCAL_TEMP_FOLDER, f"{dt:%Y-%m-%d}T000000.png")
    img_new = os.path.join(LOCAL_ARCHIVE_FOLDER, f"{sid}_{dt:%Y-%m-%d}T000000.png")

    shutil.copy(img_raw, img_new)

    # Archive data on s3
    archive_data_on_s3(sid, img_new)


def parse_arguments():
    """Parse command line arguments

    Returns:
        argparse.ArgumentParser: input arguments
    """

    parser = ArgumentParser(
        prog="ALCF",
        description="Welcome to use Automatic Lidar and Ceilometer Processing Framework (ALCF) docker container",
    )

    parser.add_argument(
        "-sid",
        "--station_id",
        required=True,
        dest="station_id",
        help="ceilometer station ID",
    )

    parser.add_argument(
        "-dt",
        "--datetime",
        required=True,
        dest="proc_time",
        help="datetime of ceilometer data",
    )

    return parser.parse_args()


def main():
    args = parse_arguments()
    run_alcf(args.station_id, datetime.strptime(args.proc_time, "%Y-%m-%d"))

    # Clean up
    client.containers.prune()


if __name__ == "__main__":
    main()

    # For test only
    # for iday in tqdm.tqdm(range(1, 23)):
    #     run_alcf("NZWRA", datetime(2021, 11, iday))

    # # Clean up
    # client.containers.prune()
