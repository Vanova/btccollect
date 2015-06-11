import threading
from queue import Queue
import time
import btc_connect

## Draft - Will need to change a lot of this :)
# Add: exceptions, loop breaks, csv reader for timer/exchange values, ...

print_lock = threading.Lock()

## exchange job with timer
def job(worker):
 if worker=='btce':t_btce()
 if worker=='bitfinex':t_bitfinex()
 if worker=='btcchina':t_btcchina()

 time.sleep(0.5)
 with print_lock:
  print(threading.current_thread().name,worker)

def t_btce():
 while True:
  btc_connect.pubapi.btce()
  time.sleep(15)
 
def t_bitfinex():
 while True:
  btc_connect.pubapi.bitfinex()
  time.sleep(15)

def t_btcchina():
 while True:
  btc_connect.pubapi.btcchina()
  time.sleep(15)

def threader():
 while True:
  worker = q.get()
  job(worker)
  q.task_done()

q = Queue()
for x in range(5):
 t = threading.Thread(target = threader)
 t.daemon = True
 t.start()

# start threads
start = time.time()
## iterate through dict/list exchanges(timer)
#for worker in range(20):
# q.put(worker)

q.put('btce')
q.put('bitfinex')
q.put('btcchina')

q.join() # at thread terminate

print('Time:',time.time()-start)
