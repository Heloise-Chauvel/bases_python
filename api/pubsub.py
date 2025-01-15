from google.cloud import pubsub_v1

PROJECT_ID = ("exelcia-heloise")
TOPIC_NAME = "rental-api"

publisher = pubsub_v1.PublisherClient()
subscriber = pubsub_v1.SubscriberClient()

def publish_message(message: str):
    topic_path = publisher.topic_path(PROJECT_ID, TOPIC_NAME)
    future = publisher.publish(topic_path, message.encode("utf-8"))
    return future.result()

def subscribe_to_message(callback):
    subscription_path = subscriber.subscription_path(PROJECT_ID, f"{TOPIC_NAME}-sub")
    streaming = subscriber.subscribe(subscription_path, callback=callback)
    return streaming