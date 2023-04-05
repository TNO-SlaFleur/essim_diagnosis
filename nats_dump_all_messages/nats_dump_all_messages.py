# pip3 install nats-python==0.8.0
import datetime
import os

from pynats import NATSClient, NATSMessage


def now() -> str:
    return datetime.datetime.now().isoformat()


nats_server = os.getenv('NATS_SERVER', 'localhost')
nats_port = os.getenv('NATS_PORT', '4222')
url = 'nats://{}:{}'.format(nats_server, nats_port)
consumer = NATSClient(url=url,
                      name='nats-consumer-diagnosis',
                      socket_keepalive=True)
consumer.connect()
print(f'{now()} Connected to {url}')


def handle_message(message: NATSMessage):
    print(f'{now()} {message.sid}, {message.subject}, {message.reply}, {message.payload.decode()}')


sub = consumer.subscribe(subject='*', callback=handle_message)
try:
    consumer.wait()
except KeyboardInterrupt:
    print('Received signal to stop. Closing...')
    consumer.unsubscribe(sub)
    consumer.close()

