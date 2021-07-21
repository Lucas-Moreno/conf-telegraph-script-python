import paho.mqtt.client as mqtt
import json, time, random
from datetime import datetime
from time import sleep
import random

#Paramètres de connexion à compléter
#Nom du groupe sans espaces avec la nomenclature WEB2 ou WEB3
#Exemple : WEB2-GROUPE3
GROUPNAME="WEB2-GROUPE13"

MQTT_BROKER="hetic.arcplex.fr"

#Login et mot de passe du groupe
MQTT_USERNAME="GROUP13"
MQTT_PASSWORD="74156626"
# un ID différent par Node
NODE_ID=["A101","A102","A103","A104","A105","A106","A107","A108","A109","A110","B101","B102","B103","B104","B105","B106","B107"]
#ID du sensor
SENSOR_ID_temperature=112
SENSOR_ID_bruit=107
SENSOR_ID_nbPers=122
SENSOR_ID_luminosite=121

client = mqtt.Client("client")
client.username_pw_set(username=MQTT_USERNAME,password=MQTT_PASSWORD)
client.connect(MQTT_BROKER)

#Type de donnée renvoyée : Random 0 ou 1



def run(condition):
    while datetime.now().minute not in {35}:
        sleep(1)
    def task():
        for node in NODE_ID:
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID_temperature)
            MQTT_MSG = json.dumps({"source_address": node, "sensor_id": SENSOR_ID_temperature, "tx_time_ms_epoch": int(time.time()),
                               "data": {"value": round(random.randint(10, 40))}})
            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s"%(node,int(time.time())))
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID_bruit)
            MQTT_MSG = json.dumps({"source_address": node, "sensor_id": SENSOR_ID_bruit, "tx_time_ms_epoch": int(time.time()),
                               "data": {"value": round(random.randint(0, 120))}})
            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s"%(node,int(time.time())))
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID_nbPers)
            MQTT_MSG = json.dumps({"source_address": node, "sensor_id": SENSOR_ID_nbPers, "tx_time_ms_epoch": int(time.time()),
                               "data": {"value": round(random.randint(0, 50))}})
            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s"%(node,int(time.time())))
            MQTT_TOPIC = GROUPNAME + "/" + node + "/" + str(SENSOR_ID_luminosite)
            MQTT_MSG = json.dumps({"source_address": node, "sensor_id": SENSOR_ID_luminosite, "tx_time_ms_epoch": int(time.time()),
                               "data": {"value": round(random.randint(0, 10000))}})
            client.publish(MQTT_TOPIC, MQTT_MSG)
            print("MQTT Mis à jour - Node %s Timestamp : %s"%(node,int(time.time())))
    task()
    while condition == True:
        sleep(60 * 15)
        task()

run(True)