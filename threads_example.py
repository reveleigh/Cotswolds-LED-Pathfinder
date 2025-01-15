from microdot import Microdot, Response
import mm_wlan
import gc
import _thread
import time
from machine import Pin

# Replace with your actual LED pins
led_pins = [Pin(2, Pin.OUT), Pin(3, Pin.OUT), Pin(4, Pin.OUT)] 

# LED control functions
def sequence_a():
  """Your LED sequence for /a"""
  while True:
    if stop_threads: 
      break
    for led in led_pins:
      led.on()
      time.sleep(0.2)
      led.off()
      time.sleep(0.2)

def sequence_b():
  """Your LED sequence for /b"""
  while True:
    if stop_threads:
      break
    for led in led_pins:
      led.on()
      time.sleep(0.5)
      led.off()
      time.sleep(0.5)

def sequence_c():
  """Turn off all LEDs"""
  for led in led_pins:
    led.off()

# Threading variables
stop_threads = False  # Global flag to signal threads to stop
threads = []  # List to keep track of running threads

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

@app.route('/a')
def route_a(request):
  global stop_threads, threads
  stop_threads = True 
  for t in threads: 
    t.join()
  stop_threads = False 
  threads.append(_thread.start_new_thread(sequence_a, ()))
  return "Sequence A started", 200

@app.route('/b')
def route_b(request):
  global stop_threads, threads
  stop_threads = True
  for t in threads:
    t.join()
  stop_threads = False
  threads.append(_thread.start_new_thread(sequence_b, ()))
  return "Sequence B started", 200

@app.route('/c')
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