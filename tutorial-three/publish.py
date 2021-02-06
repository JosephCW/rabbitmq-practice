#!/usr/bin/env python
import pika

# credentials to connect. defaults to 'guest' 'guest'
credentials = pika.credentials.PlainCredentials('price-scraper-username', 'price-scraper-password', erase_on_connect=True)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='alerts', exchange_type='fanout')

message = 'Hello World Subscribers'
# routing key ignored for all fanout exchanges
channel.basic_publish(exchange='alerts', routing_key='', body=message)
print('Sent hello world message')
connection.close()