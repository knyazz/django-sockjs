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
python
```
