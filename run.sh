#!/usr/bin/env bash
set -e
docker build -t humblehound/pythonparser:latest .
docker rm parser
docker run --name=parser humblehound/pythonparser:latest