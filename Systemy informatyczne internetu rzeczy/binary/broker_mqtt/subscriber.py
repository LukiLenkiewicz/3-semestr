import paho.mqtt.client as mqtt
import requests

mqttBroker ="mqtt.eclipseprojects.io"


def on_connect(client, userdata, flags, rc):
    client.subscribe("disc_usage")


def on_message(client, userdata, message):
    info = message.payload.decode()
    print(info)
    requests.post('http://127.0.0.1:5000/', data=info)


client = mqtt.Client("Subscriber")
client.connect(mqttBroker, 1883) 


client.on_connect = on_connect
client.subscribe("disc_usage")
client.on_message = on_message

client.loop_forever()
