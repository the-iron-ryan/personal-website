FROM python:3.9

# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

COPY requirements.txt .
# install python dependencies
RUN pip install --upgrade pip
RUN pip install --no-cache-dir -r requirements.txt

COPY . .

# TODO: Ensure ImageMagick AND (possibly?) Ghostscript is installed

# FROM debian:bullseye-slim

# # Install ImageMagick
# RUN apt-get update && \
#     apt-get install -y imagemagick && \
#     rm -rf /var/lib/apt/lists/*

# OR

# FROM alpine:latest

# # Install ImageMagick
# RUN apk --no-cache add imagemagick



# running migrations
RUN python manage.py migrate

# gunicorn
CMD ["gunicorn", "--config", "gunicorn-cfg.py", "core.wsgi"]
