import sys
import threading
from queue import Queue
import time
import btc_connect

## To Do: exceptions, loop breaks, csv reader for timer values & trades (config), various commands...

print_lock = threading.Lock()

## exchange job with timer
def job(worker):
 if worker=='btce':t_btce()
 if worker=='bitfinex':t_bitfinex()
 if worker=='btcchina':t_btcchina()

 time.sleep(0.1)
 with print_lock:
  print(threading.current_thread().name,worker)


# todo: hese should push threads and then delay to avoid the delay of the function.
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

def main(args):
 #rework for delay compensation
	start = time.time() # start threads

	q.put('btce')
	q.put('bitfinex')
	q.put('btcchina')

	q.join() # at thread terminate

	print('Time:',time.time()-start)

q = Queue()
for x in range(5):
 t = threading.Thread(target = threader)
 t.daemon = True
 t.start()
	 
if __name__ == '__main__':
    main(sys.argv[1:])
