FROM humblehound/yaafe-docker

MAINTAINER Humblehound <dejtabejz@gmail.com>

CMD "mkdir app"
COPY parser.py app/
WORKDIR app/
EXPOSE 80
ENTRYPOINT ["python", "parser.py"]