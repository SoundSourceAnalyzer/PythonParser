FROM humblehound/yaafe-docker

MAINTAINER Humblehound <dejtabejz@gmail.com>

EXPOSE 80
RUN mkdir -p app/genres
WORKDIR app
COPY parser.py .
ENTRYPOINT ["python","parser.py"]