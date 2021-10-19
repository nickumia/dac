FROM ubuntu:bionic

RUN apt update && \
		apt-get install python3-pip -y

