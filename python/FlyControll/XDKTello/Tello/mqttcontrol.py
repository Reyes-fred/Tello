from time import sleep
import signal
import tellopy
import paho.mqtt.client as paho
import sys

from threading import Thread

mqttserver = "broker.hivemq.com"
mqttport = 1883
drone = tellopy.Tello()

def handler(event, sender, data, **args):
   drone = sender
   if event is drone.EVENT_FLIGHT_DATA:
      print(data)

def subscribeTelloAction(mosq, obj, msg):
   print("Command %s" % msg.payload)
   if msg.payload == "takeoff":
      drone.takeoff()
      sleep(5)
   elif msg.payload == "land":
      drone.land()
      sleep(5)
      drone.quit()
   elif msg.payload == "left":
      drone.left(30)
      sleep(4)
   elif msg.payload == "right":
      drone.right(30)
      sleep(4)
   elif msg.payload == "forward":
      drone.forward(30)
      sleep(4)
   elif msg.payload == "back":
      drone.back(30)
      sleep(4)
   elif msg.payload == "up":
      drone.up(30)
      sleep(4)
   elif msg.payload == "down":
      drone.down(30)
      sleep(4)
   elif msg.payload == "cw":
      drone.cw(180)
      sleep(4)
   elif msg.payload == "ccww":
      drone.ccw(180)
      sleep(4)
   elif msg.payload == "flip":
      drone.flip(r)
      sleep(4)

def subscribeTello():
   mqttclient = paho.Client()
   mqttclient.on_message = subscribeTelloAction
   mqttclient.connect(mqttserver, mqttport, 60)
   mqttclient.subscribe("xdk110/tello/action", 0)
   while mqttclient.loop() == 0:
      pass

def functionSignalHandler(signal, frame):
   sys.exit(0)

if __name__ == '__main__':
   signal.signal(signal.SIGINT, functionSignalHandler)

   threadmqttsubscribetello = Thread(target=subscribeTello)
   threadmqttsubscribetello.start()
   try:
      drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)
      drone.connect()
      drone.wait_for_connection(60.0)
   except Exception as ex:
      print(ex)
   while True:
      time.sleep(5)
