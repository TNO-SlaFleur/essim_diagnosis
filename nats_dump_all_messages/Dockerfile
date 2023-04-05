FROM python:3.10-slim

COPY ./nats_dump_all_messages.py ./
RUN pip3 install nats-python==0.8.0

ENTRYPOINT ["python3", "nats_dump_all_messages.py"]
