FROM ubuntu:20.04 AS base

ARG DEBIAN_FRONTEND="noninteractive"

RUN apt-get update && apt-get install -y gfortran libexpat-dev m4 libcurl4-openssl-dev zlib1g-dev \
    python3-setuptools python3-pip libeccodes-tools unzip wget && rm -rf /var/lib/apt/lists/* \
    /tmp/* /var/tmp/*

COPY alcf_docker /root/alcf

WORKDIR /root/alcf

RUN bash download_dep
RUN bash build_dep
RUN make

RUN python3 setup.py install

COPY entrypoint.sh /root/alcf/

ENTRYPOINT [ "./entrypoint.sh" ]