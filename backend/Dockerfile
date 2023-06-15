FROM python:3.10.6

WORKDIR /code

COPY ./ /code/backend

RUN pip install --no-cache-dir --upgrade -r /code/backend/requirements.txt

EXPOSE 8080

WORKDIR /code/backend