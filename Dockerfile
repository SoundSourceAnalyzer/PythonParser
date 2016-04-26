FROM humblehound/yaafe-docker

MAINTAINER Humblehound <dejtabejz@gmail.com>

CMD "mkdir app"
WORKDIR app/
EXPOSE 80
COPY parser.py .
ENTRYPOINT ["python", "parser.py"]