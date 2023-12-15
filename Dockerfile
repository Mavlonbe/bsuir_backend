FROM python:3.8.5-slim-buster

WORKDIR /usr/src/app

RUN pip install --upgrade pip
COPY ./requirements.txt /usr/src/app/requirements.txt
RUN pip install -r requirements.txt

COPY . /usr/src/app/

ENV SERVICE_STATE production

CMD ["uvicorn", "notes.asgi:application", '--host "0.0.0.0"', "--port 23335"]
