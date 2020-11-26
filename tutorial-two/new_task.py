#!/usr/bin/env python
import sys, pika


# Take arguments from command line and send to rabbit, or 'Hello World'
message = ''.join(sys.argv[1:] if len(sys.argv) > 1 else []) or 'Hello World'

# Connect to rabbitmq and send message
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

channel.basic_publish(exchange='',
        routing_key='hello',
        body=message)
print('[x] Sent: %r' % message)

