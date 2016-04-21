#!/usr/bin/env bash
set -e
docker build -t humblehound/pythonparser:latest .
docker run --name=parser --rm -v $(pwd)/data:/app/data -v $(pwd)/results:/app/results humblehound/pythonparser:latest
