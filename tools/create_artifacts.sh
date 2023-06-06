#!/usr/bin/bash

set +xe
set -x

host=$1

[ ! -d tool/ ] && mkdir tool/
go build -o tool/
cp .conf/example.toml tool/
tar cvfz hooklistener.tar.gz tool/
scp hooklistener.tar.gz ${host}:~/

ssh ${host} 'bash -c "tar xvfz hooklistener.tar.gz"'
rm -rf tool/
