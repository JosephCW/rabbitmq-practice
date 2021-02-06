#!/usr/bin/env python
import pika

# credentials to connect. defaults to 'guest' 'guest'
credentials = pika.credentials.PlainCredentials('price-scraper-username', 'price-scraper-password', erase_on_connect=True)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))

channel = connection.channel()
# If the exchange isn't there, create it since we don't want code below to error
channel.exchange_declare(exchange='alerts', exchange_type='fanout')

# Create a queue specifically for this subscribe instance
result = channel.queue_declare(queue='', exclusive=True)
# Get the uniquely generated name given to this instance
queue_name = result.method.queue
# Bind our queue to the exchange so the fanout alerts will be sent to our queue
channel.queue_bind(exchange='alerts', queue=queue_name)

print('Waiting for an alert...')

def callback(ch, method, properties, body):
    print('[x] %r' %body)

# bind our channel to the queue along with callback func
channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True
)

channel.start_consuming()