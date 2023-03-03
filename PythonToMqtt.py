import paho.mqtt.client as mqttclient
import time
import json
import random



def on_connect(client,userdata,flags,rc):
    if rc==0:
        print("Client is Connected")
        global connected
        connected=True
    else:
        print("Connection Failed")
        return data


def on_message(client,userdata,message):
    print("Message Recieved",str(message.payload.decode("utf-8")))
    print("message topic=",message.topic)


    
Messagerecieved=False
connected=False
broker_address='broker.mqttdashboard.com'
port=8000
user='user_name'
password='password'



client=mqttclient.Client("MQTT")
client.on_connect=on_connect
client.on_message=on_message
client.username_pw_set(user,password=password)
client.connect(broker_address,port=port)
client.loop_start()
client.subscribe("test/mqtt")


while connected!=True:
    
    data={}
    data["Name"]="Raj"
    time.sleep(1)

    #Convert Dictionary to JSON 
    #json_object = json.dumps(data, indent = 3)
 
    
    print(json_object)
    client.publish('topic',data)    

    
while Messagerecieved!=True:
    time.sleep(1)
    client.loop_stop()
