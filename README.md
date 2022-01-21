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
        "USER": "guest",
        "PASSWORD": "guest",
        "SERVER": {
            "HOST": "localhost",
            "PORT": 5672,
            "VHOST": "/"
        },
        "EXCHANGE_NAME": "sockjs",
        "EXCHANGE_TYPE": "direct",
        "QUEUE_NAME": "ws01"
    },
    'REDIS_SERVER': {
        "HOST": "localhost",
        "PORT": 6379,
        "DB": 0,
        "PASSWORD": None,
        "PREFIX": "sockjs:"
    },
    'HOST': '0.0.0.0',
    'PORT': 8083,
    'LOCATION': '/ws',
    'SECRET_KEY': 'PLEASE_SET'
}
```
