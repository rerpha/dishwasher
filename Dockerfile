FROM python:3.8-slim-buster

WORKDIR /app

RUN pip3 install Flask

COPY . .

EXPOSE 80

CMD [ "python3", "-m" , "flask", "run", "--host=192.168.0.80", "--port=80"]

