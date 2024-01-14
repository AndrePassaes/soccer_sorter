# Use an official Python runtime as a parent image
FROM python:3.9

# Set work directory
WORKDIR /soccer_sorter

RUN groupadd soccer_sorter && useradd soccer_sorter -g soccer_sorter

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

#Install PostgreSQL dependecies
RUN apt-get update \
    && apt-get install -y postgresql gcc \
    && apt-get clean \
    && rm -rf /var/lib/apt/lists/*

#Update pip
RUN pip install --upgrade pip

# Install dependencies
COPY ./requirements.txt /soccer_sorter/requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

# Copy the current directory contents into the container at /soccer_sorter
COPY . /soccer_sorter/
