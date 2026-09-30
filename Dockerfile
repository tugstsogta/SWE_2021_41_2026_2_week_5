FROM ubuntu:22.04
RUN apt-get update && apt-get install -y python3
WORKDIR /app
COPY bind_mount/ /app/bind_mount/
CMD ["python3", "/app/bind_mount/ishappy.py"]