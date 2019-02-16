#!/bin/bash
docker start jenkins-master || \
    docker run -t -p 8080:8080 -p 50000:50000 -d --name jenkins-master myjenkins:latest

