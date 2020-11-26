#!/usr/bin/env python
import pika

# ConnectionParameters accepts IP or hostnames
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
channel = connection.channel()

# Create a queue so RabbitMQ doesn't just drop the message
channel.queue_declare(queue='hello')

# A message can't be sent directly to a queue, needs to go through an exchange
# Use default exchange "''", default allows specification of which queue
channel.basic_publish(exchange='',
        routing_key='hello',
        body='Hello World!')
print("[x] Sent 'Hello World!'")

# Flush network buffers, verify that message actually delivered.
connection.close()

