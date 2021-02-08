#!/usr/bin/env python
import pika

# credentials to connect. defaults to 'guest' 'guest'
credentials = pika.credentials.PlainCredentials('price-scraper-username', 'price-scraper-password', erase_on_connect=True)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()

# Topic allows for the equiv of dynamic 'routing keys'
# 'routing key' is '.' separated. '*' symbol to match a word, # to match rest of key
channel.exchange_declare(exchange='topic_logs', exchange_type='topic')

#    'apples',
#    '*.bees.*',
#    'programming.*',
#    'atom.#',
#    'atomizer#',

topics = [
    'apples.fruit', # does not make it through
    'programming.bananas', # makes it through
    'abc.bees.def' # does not make it through
    'atom' # does not make it through
    'atom.apples' # does not make it through
    'atomizer' # does not make it through
]

for topic in topics:
    message = 'Hello using routing key %s' %topic
    channel.basic_publish(
        exchange='topic_logs', routing_key=topic, body=message
    )
    print('Sent %s to %s' %(message, topic))

connection.close()