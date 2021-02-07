#!/usr/bin/env python
import pika
from random import randint

# credentials to connect. defaults to 'guest' 'guest'
credentials = pika.credentials.PlainCredentials('price-scraper-username', 'price-scraper-password', erase_on_connect=True)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))

channel = connection.channel()

channel.exchange_declare(exchange='alerts', exchange_type='direct')

randomNumber = randint(0, 1)
severity = 'high' if randomNumber else 'low'

message = 'Hello World to severity %s channel' %severity
# 
channel.basic_publish(exchange='alerts', routing_key=severity, body=message)
print('Sent hello world message')
connection.close()