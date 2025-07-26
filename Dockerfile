FROM rasa/rasa:3.6.21-full

WORKDIR /app
COPY . /app

EXPOSE 5005