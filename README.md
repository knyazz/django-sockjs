# ampq-websockets
Websocket server based on websockets using ampq protocol for messaging

Tested on python 3.9.9

## Requirements:

* redis >= 2.9.1
* pika >= 1.2.0
* websockets >= 10.1


## Installation:
```
pip install py-ampq-websockets-server
```

## Usage:

### Subscribing to room
Browser -> (subcribing to room) -> py-sockjs -> (assign id and add) -> redis

### Sending data to room
1. Py Framework -> (get connect by room) -> redis

  (
    Django,
    Flask
    and etc.
  )

2. Py Framework -> (put data) -> rabbitmq -> (data) -> py-sockjs -> (send data) -> Browser

Run
```
python src/ampq_websockets/runserver.py
```

## Optional

### Django integration

1. Make Command in the project: <any_app>/management/command/websocket_server.py
```
from django.conf import settings

import ampq_websockets

class Command(BaseCommand):
    def handle(self, *args, **options):
        logger = logging.getLogger(__name__)
        logger.info('start django-websocket-server')
        ampq_websockets.start(settings.DJANGO_WEBSOCKET_SERVER)
```

2. Make DJANGO_WEBSOCKET_SERVER in settings.py. Example:
```
DJANGO_WEBSOCKET_SERVER = {
    'RABBIT_SERVER': {
        'server_host': 'rabbit0',
        'host': 'rabbit0',
        'user': 'guest',
        'password': 'guest',
        'port': 5672,
        'vhost': '/',
        'exchange_name': 'sockjs',
        'queue_name': 'ws01',
        'exchange_type': 'direct',
    },
    'REDIS_SERVER': {
        'host': 'redis0',
        'port': '6379',
        'db': 1,
    },
    'listen_addr': '0.0.0.0',
    'listen_port': 8083,
    'listen_location': '/ws',
    'secret_key': 'xe4pa7gysp4phe2rhyd',
    'sockjs_url': ['ws://localhost:8083/ws']
}
```
