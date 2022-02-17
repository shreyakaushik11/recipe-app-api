FROM python:3.10-alpine

ENV PYTHONUNBUFFERED 1 
#tells python to run in unbuffered mode 

COPY ./requirements.txt /requirements.txt
#it copies under the docker image
RUN apk add --update --no-cache postgresql-client jpeg-dev
RUN apk add --update --no-cache --virtual .tmp-build-deps \
    gcc libc-dev linux-headers postgresql-dev musl-dev zlib zlib-dev

RUN pip install -r /requirements.txt
RUN apk del .tmp-build-deps

RUN mkdir /app
#it creates an empty folder on our docker image
WORKDIR /app
#it switches to default directory so any application we run using our docker container will run starting from this location 
COPY ./app /app
#it copies from our local machine app folder to the app folder we created on our image

RUN mkdir -p /vol/web/media
RUN mkdir -p /vol/web/static
RUN adduser -D user
#here we've created a user that's going to run our application using docker
RUN chown -R user:user /vol/
RUN chmod -R 755 /vol/web
USER user
#now we've switched to user we created
#this is done for security purpose, if we don't do it then the application is run thru the root account
