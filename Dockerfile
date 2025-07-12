# syntax=docker/dockerfile:1

# Comments are provided throughout this file to help you get started.
# If you need more help, visit the Dockerfile reference guide at
# https://docs.docker.com/go/dockerfile-reference/

# Want to help us make this template better? Share your feedback here: https://forms.gle/ybq9Krt8jtBL3iCk7

ARG PYTHON_VERSION=3.13
FROM python:${PYTHON_VERSION}-slim as base

# Prevents Python from writing pyc files.
ENV PYTHONDONTWRITEBYTECODE=1

# Keeps Python from buffering stdout and stderr to avoid situations where
# the application crashes without emitting any logs due to buffering.
ENV PYTHONUNBUFFERED=1

# Install system packages.
RUN apt-get update --yes --quiet && apt-get install --yes --quiet --no-install-recommends \
    build-essential \
    curl \
    net-tools \
    iputils-ping \
    git \
    software-properties-common \
    libjpeg62-turbo-dev \
    zlib1g-dev \
    libwebp-dev \
    python3-pip \
    python3-dev \
    libpq-dev \
    postgresql-client \
    gdal-bin libgdal-dev \
    python3-gdal \
    binutils \
    libproj-dev \
    && rm -rf /var/lib/apt/lists/*

WORKDIR /app

# Copy the source code into the container.
COPY . .

# Download dependencies as a separate step to take advantage of Docker's caching.
# Leverage a cache mount to /root/.cache/pip to speed up subsequent builds.
# Leverage a bind mount to requirements.txt to avoid having to copy them into
# into this layer.
RUN --mount=type=cache,target=/root/.cache/pip \
    --mount=type=bind,source=requirements.txt,target=requirements.txt \
    python -m pip install -r requirements.txt

ENV PYTHONPDB=/tmp/.pdbhistory
RUN touch /.pdbhistory && chmod 666 /.pdbhistory

# Expose the port that the application listens on.
EXPOSE 8000

# Run the application.
CMD yes
