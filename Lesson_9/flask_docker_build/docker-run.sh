#!/bin/bash
docker build -t class-9-flask  .
docker stop $(docker ps -a -q)
docker rm $(docker ps -a -q)
docker run -d -p 5001:5001 class-9-flask