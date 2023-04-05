


# To run
```bash
docker build -t nats_dump_messages ./
docker run -e NATS_SERVER=localhost -e NATS_PORT=4222 --rm -ti --network host nats_dump_messages
```