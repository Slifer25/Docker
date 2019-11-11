FROM python:3.7

# Copy full application to the image
# For real environments, consider customize .dockerignore
COPY src /opt/application

# This is to make it easier. The defaul PWD where you
# start when using your application
WORKDIR /opt/application

RUN pip install -r requirements.txt

# Run default flask, but allow remote access
CMD flask run --host=0.0.0.0


