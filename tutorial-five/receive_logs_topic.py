#!/usr/bin/env python
import pika

# credentials to connect. defaults to 'guest' 'guest'
credentials = pika.credentials.PlainCredentials('price-scraper-username', 'price-scraper-password', erase_on_connect=True)
connection = pika.BlockingConnection(pika.ConnectionParameters('localhost', credentials=credentials))
channel = connection.channel()

channel.exchange_declare(exchange='topic_logs', exchange_type='topic')
result = channel.queue_declare('', exclusive=True)
queue_name = result.method.queue

bind_words = [
    'apples',
    '*.bees.*',
    'programming.*',
    'atom.#',
    'atomizer#',
]

for binding_key in bind_words:
    channel.queue_bind(exchange='topic_logs', queue=queue_name, routing_key=binding_key)

print('Waiting for mesage. Bound to queues: %s' %bind_words)

def callback(ch, method, properties, body):
    print('%r:%r' %(method.routing_key, body))

channel.basic_consume(
    queue=queue_name, on_message_callback=callback, auto_ack=True
)

channel.start_consuming()
