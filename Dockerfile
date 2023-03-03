# Start from debian linux image (DockerHub)
FROM debian:stable

# Add custom label
LABEL maintainer "Laura Escudero <laura.escudero@uvic.cat>" \
      version "0.1" \
      description "Docker image for running seqClass.py - Hands on practical"

# Install Python (after apt-get update)
RUN apt-get update && apt-get install -y --no-install-recommends \
         python-is-python3

# Make the folder '/scripts' in the container
RUN mkdir /scripts

# Copy 'seqClass.py' to the folder '/scripts' in the container
ADD seqClass.py /scripts
