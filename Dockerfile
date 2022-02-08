FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1 
#tells python to run in unbuffered mode 

COPY ./requirements.txt /requirements.txt
#it copies under the docker image
RUN apk add --update --no-cache postgresql-client
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
#it creates an empty folder on our docker image
WORKDIR /app
#it switches to default directory so any application we run using our docker container will run starting from this location 
COPY ./app /app
#it copies from our local machine app folder to the app folder we created on our image

RUN adduser -D user
#here we've created a user that's going to run our application using docker

USER user
#now we've switched to user we created
#this is done for security purpose, if we don't do it then the application is run thru the root account
