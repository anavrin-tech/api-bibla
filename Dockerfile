FROM python:3.9.1-slim

# Upgrade pip
RUN pip install --upgrade pip

# Make a local directory
RUN mkdir /app

# set "app" as the working directory from which CMD, RUN, ADD references
WORKDIR /app

# now copy all the files in this directory to /code
ADD . .

# pip installl the local requirements.txt
RUN pip install -r requirements.txt

# Define our command to be run when lauching the container
CMD uvicorn main:app --host 0.0.0.0 --port $PORT