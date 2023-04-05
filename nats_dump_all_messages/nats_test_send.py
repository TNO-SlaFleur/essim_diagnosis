# pip install nats-python
import datetime
import os

from pynats import NATSClient, NATSMessage


def now() -> str:
    return datetime.datetime.now().isoformat()


nats_server = os.getenv('NATS_SERVER', 'localhost')
nats_port = os.getenv('NATS_PORT', '4222')
url = 'nats://{}:{}'.format(nats_server, nats_port)
connection = NATSClient(url=url,
                        name='nats-producer-diagnosis',
                        socket_keepalive=True)
connection.connect()
print(f'{now()} Connected to {url}')

connection.publish(subject='test-subject/somwhere',
                   payload='hello!'.encode())

connection.close()

