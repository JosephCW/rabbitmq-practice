#!/usr/bin/env python
import pika, sys, os


def main():
    connection = pika.BlockingConnection(pika.ConnectionParameters('localhost'))
    channel = connection.channel()
    
    # Method that will be used as the callback whenever a message is received from queue
    def callback(ch, method, properties, body):
        print('[x] Received: %r' % body)
    
    # channel to receive on, only have to declare because unsure if it actually exists yet.
    channel.queue_declare(queue='hello')
    channel.basic_consume(queue='hello',
            auto_ack=True,
            on_message_callback=callback)

    # Go into waiting state to repeatedly call 'callback' when a new message is retrieved
    print('[*] Waiting for message. to exit press CTRL+C')
    channel.start_consuming()


if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        print('Interrupted')
        try:
            sys.exit(0)
        except SystemExit:
            os._exit(0)

