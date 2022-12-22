import paho.mqtt.client as mqtt
import json
import requests

mqtt_sub_topic="mqtt/avirup171/#"
client=mqtt.Client()
edgeDeviceSendTopic="mqtt/avirup171/edgeDevice"
edgeDeviceReceiveTopicBase="mqtt/avirup171/"
serverUrl="http://127.0.0.1:5000/telemetrysink"
headers =  {"Content-Type":"application/json"}

def on_connect(client, userdata, flags, rc):
    client.connected_flag=True
    client.disconnect_flag=False
    client.subscribe(mqtt_sub_topic)
    print("Connected")
    print("rc: " + str(rc))


def on_subscribe(client, userdata, mid, granted_qos):
    print("Subscribed: " + str(mid) + " " + str(granted_qos)+" "+"Topic: "+mqtt_sub_topic)

def on_disconnect(client, userdata, rc):
    print("disconnecting reason  "  +str(rc))
    client.connected_flag=False
    client.disconnect_flag=True

def on_message(client, userdata, message):
    print("message received  ",str(message.payload))
    print("message topic  ",str(message.topic))
    rawPayloadData= message.payload.decode('UTF-8')
    topic = str(message.topic)
    print(topic)
    if(topic=="mqtt/avirup171/edgeDevice"):
        jsonData=json.dumps(rawPayloadData)
        response=requests.post(serverUrl,jsonData,headers=headers)
        responseData=response.json()
        device_id=responseData["device_id"]
        pubTopic=edgeDeviceReceiveTopicBase+device_id
        client.publish(pubTopic,str(responseData))
        print(responseData)


def init_mqtt(client,mqtt_host,mqtt_port):
    mqtt.Client.connected_flag=False

    client.on_connect = on_connect  
    client.on_subscribe=on_subscribe
    client.on_message=on_message
    client.connect(mqtt_host, int(mqtt_port))

def handler():
    mqtt_host="broker.hivemq.com"
    mqtt_port="1883"
    #Connection initiated
    init_mqtt(client,mqtt_host,mqtt_port)
    client.loop_forever()

if __name__ == "__main__": 
    handler()