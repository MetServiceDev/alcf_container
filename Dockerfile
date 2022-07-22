FROM ubuntu:20.04 AS base

ARG DEBIAN_FRONTEND="noninteractive"

# ENV TZ=Asia/Dubai
ENV TZ=UTC
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

RUN apt-get update && apt-get install -y gcc make gfortran libhdf5-dev libnetcdf-dev \
    libnetcdff-dev python3 python3-setuptools python3-pip && rm -rf /var/lib/apt/lists/* \
    /tmp/* /var/tmp/*

RUN pip3 install alcf --upgrade

COPY entrypoint.sh /root/
RUN chmod 755 /root/entrypoint.sh

WORKDIR /root
RUN mkdir lidar
RUN mkdir plot

ENTRYPOINT [ "./entrypoint.sh" ]