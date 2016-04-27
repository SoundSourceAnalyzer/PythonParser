#!/usr/bin/env bash
#set -e
docker build -t humblehound/pythonparser:latest .
docker run --rm --name=parser -v /opt/genres/:/app/genres humblehound/pythonparser:latest