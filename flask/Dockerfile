FROM python:3.6
WORKDIR /var/www/app

COPY ./requirements.txt requirements.txt
RUN pip install -r requirements.txt

WORKDIR /var/www/app

EXPOSE 5000
CMD [ "uwsgi", "--ini", "uwsgi.ini" ]