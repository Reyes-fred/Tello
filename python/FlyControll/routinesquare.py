from time import sleep
import tellopy


def handler(event, sender, data, **args):
   drone = tellopy.Tello()
   try:
     drone.subscribe(drone.EVENT_FLIGHT_DATA, handler)

     drone.connect()
     drone.wait_for_connection(60.0)
     drone.takeoff()
     sleep(5)
     drone.forward(30)
     sleep(5)
     drone.right(30)
     sleep(5)
     drone.back(30)
     sleep(5)
     drone.left(30)
     sleep(5)
     drone.land()
   except Exception as ex:
      print(ex)
   finally:
      drone.quit()

if __name__ == '__main__':
   test()
