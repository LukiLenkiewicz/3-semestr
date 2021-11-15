import paho.mqtt.client as mqtt
import shutil
import time
import json

mqttBroker = "mqtt.eclipseprojects.io"

client = mqtt.Client("Disc_usage")
client.connect(mqttBroker, 1883)

total, prev_used, free = shutil.disk_usage("/")

while True:
    total, used, free = shutil.disk_usage("/")
    time_stamp = time.time()
    if abs(used - prev_used) > 100:
        data = {}
        data[time_stamp] = used
        content = json.dumps(data)
        client.publish("disc_usage", content)
        print(f"opubliowano {used}, {time_stamp}")
        prev_used = used
    time.sleep(1)