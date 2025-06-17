import pika
import json

def publish_client_created(data):
    connection = pika.BlockingConnection(pika.ConnectionParameters('rabbitmq'))
    channel = connection.channel()
    channel.queue_declare(queue='client_created')

    message = json.dumps(data)
    channel.basic_publish(exchange='', routing_key='client_created', body=message)
    print(f"[🐰] Message envoyé : {message}")
    connection.close()
