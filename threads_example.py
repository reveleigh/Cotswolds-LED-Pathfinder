from microdot import Microdot, Response
import mm_wlan
import gc
import _thread
import time
from machine import Pin
from dijkstra import dijkstra
from cotswolds import towns



def astar():
  while True:
    if stop_threads:
      break
    # Placeholder text for now
    print("A*")
    time.sleep(1)

def sequence_c():
  """Turn off all LEDs"""
  for led in led_pins:
    led.off()

# Threading variables
stop_threads = False  # Global flag to signal threads to stop
threads = []  # List to keep track of running threads

# Call back to get status of stop_threads
def stop_callback():
    return stop_threads


# Wi-Fi credentials
ssid = 'Wifi name' 
password = 'password'

app = Microdot()

# Connect to Wi-Fi with logging
try:
  mm_wlan.connect_to_network(ssid, password)
  print("Connected to Wi-Fi!")  # Log success
except Exception as e:
  print(f"Error connecting to Wi-Fi: {e}")  # Log error

@app.route('/')
def index(request):
    return 'Hello, from Pico'

@app.route('/dijkstra')
def route_a(request):
  global stop_threads, threads
  stop_threads = True 
  for t in threads: 
    t.join()
  stop_threads = False 
  threads.append(_thread.start_new_thread(dijkstra, (towns, stop_callback)))
  return "Dijkstra started", 200

@app.route('/astar')
def route_b(request):
  global stop_threads, threads
  stop_threads = True
  for t in threads:
    t.join()
  stop_threads = False
  threads.append(_thread.start_new_thread(astar, ()))
  return "Lights turned off", 200

@app.route('/off')
def route_c(request):
  global stop_threads, threads
  stop_threads = True
  for t in threads:
    t.join()
  sequence_c()
  return "All LEDs off", 200

@app.route('memory')
def memory(request):
    response = '<h1>Free Memory={} bytes</hi>'.format(gc.mem_free())
    return response, {'Content-Type': 'text/html'}

app.run(port=80)