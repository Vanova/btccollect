import urllib.request, urllib.parse, urllib.error
import http.client
# import simplejson as json    
import json			# replace w/ ujson or simplejson? (needs C binary)
import pprint
import hashlib
import hmac
import time
import jsonfilter

class pubapi():

 def connects(url, con_list, meth, pair):
  sconn = http.client.HTTPSConnection(url)
  jsdata = []
  for path in range(len(con_list)):
   sconn.request("GET", con_list[path])
   response = sconn.getresponse().read().decode()
   jsdata.append(json.loads(response))
   print(url+con_list[path])
  jsonfilter.filters.jfstart(url,meth,pair,jsdata)

 sconn.close()
 #end connects

 def btce(url = "btc-e.com"):
  # limited to 15sec
  methods = ['ticker', 'depth']; # 'trades' (removing for now)
  pairs = ['btc_usd', 'eur_usd', 'btc_eur'];
  pairstring = "-".join(pairs)
  params = {"limit" : 2000, "ignore_invalid" : 1}
  url_values = urllib.parse.urlencode(params)
  con_list = []
  for meth in range(len(methods)):
   con_list.append("/api/3/%s" % methods[meth] + "/" + pairstring + "?" + url_values)
  pubapi.connects(url, con_list, methods, pairs)
<<<<<<< HEAD
  
=======

>>>>>>> 0f78bbaab9cb0f2b031812a5ceab2a9a80f197bd
 def bitfinex(url = "api.bitfinex.com"):
  ## ~1/sec
  ## https://api.bitfinex.com/v1/pubticker/btcusd
  ## btcusd, ltcusd, ltcbtc, drkusd, drkbtc
  methods = ['pubticker', 'book']; # 'trades' (removing for now)
  pairs = ['btcusd', 'drkusd', 'drkbtc'];
  params = {"limit_bids" : 2000, "limit_asks" : 2000}
  url_values = urllib.parse.urlencode(params)
  con_list = []
  for meth in range(len(methods)):
   for pair in range(len(pairs)):
    con_list.append("/v1/%s" % methods[meth] + "/" + pairs[pair] + "?" + url_values)
  pubapi.connects(url, con_list, methods, pairs)

 def btcchina(url = "data.btcchina.com"):
  ## ~1/sec
  ## https://data.btcchina.com/data/orderbook?market=btccny&limit=5000
  ## market=all (ticker only?)
  ## limit=10000 (trades)	 ## limit=5000 ask/bid
  ## btccny, ltccny, btcltc
  methods = ['orderbook']; # 'trades' (removing for now)
  pairs = ['btccny', 'ltccny', 'btcltc'];  ## , "ltccny", "btcltc"
  params = {"limit" : 5000}
  ob_values = urllib.parse.urlencode(params)
  tparams = {"limit" : 10000}
  trades_values = urllib.parse.urlencode(tparams)
  con_list = []
  ## Ticker (breaks filter)
<<<<<<< HEAD
  # pubapi.connects(url, "/data/ticker?market=all", "ticker", ("ticker_" for n in range(len(pairs))))
  con_list = []
=======
  #pubapi.connects(url, "/data/ticker?market=all", "ticker", ("ticker_" for n in range(len(pairs))))
  con_list.append("/data/ticker?market=all") # could break if more trades added
>>>>>>> 0f78bbaab9cb0f2b031812a5ceab2a9a80f197bd
  for pair in range(len(pairs)):
   con_list.append("/data/%s" % methods[0] + "?market=" + pairs[pair] + "&" + ob_values)
  #for pair in range(len(pairs)): 
   #con_list.append("/data/%s" % methods[1] + "?market=" + pairs[pair] + "&" + trades_values)
  pubapi.connects(url, con_list, methods, pairs)

 ## Not using - market depth too shallow
 def kraken(url = "api.kraken.com"):
  ## ~1/sec
  ## https://api.kraken.com/0/public/AssetPairs
  ## https://api.kraken.com/0/public/Ticker?pair=XXBTZUSD,XXBTZEUR
  ## https://api.kraken.com/0/public/Depth?pair=XXBTZUSD&count=
  ## XXBT, ZUSD, ZEUR, XLTC
  methods = ['Depth', 'Trades'];
  pairs = ['XXBTZUSD', 'XXBTZEUR', 'XXBTZGBP'];
  pairstring = ",".join(pairs)
  pubapi.connects(url, "/0/public/Ticker" + "?pair=" + pairstring, "Ticker", pairs)
 	 for meth in range(len(methods)):
   for pair in range(len(pairs)):
    path = "/0/public/%s" % methods[meth] + "?pair=" + pairs[pair]
    pubapi.connects(url, path, methods[meth], pairs[pair])

###
## for testing
#pubapi.btce()
#pubapi.bitfinex()
#pubapi.btcchina()
#pubapi.kraken()

############ For Private API ##############
### Code From:
# -*- coding: utf-8 -*-
## Author:      t0pep0
## e-mail:      t0pep0.gentoo@gmail.com
## Jabber:      t0pep0@jabber.ru
## BTC   :      1ipEA2fcVyjiUnBqUx7PVy5efktz2hucb
## donate free =)
class privapi():
 __api_key	= '';
 __api_secret	= '';
 __nonce_v	= 1;
 __wait_for_nonce = False

 def __init__(self,api_key,api_secret,wait_for_nonce=False):
  self.__api_key = api_key
  self.__api_secret = api_secret
  self.__wait_for_nonce = wait_for_nonce

 def __nonce(self):
   if self.__wait_for_nonce: time.sleep(1)
   self.__nonce_v = str(time.time()).split('.')[0]

 def __signature(self, params):
  sig = hmac.new(self.__api_secret.encode(), params.encode(), hashlib.sha512)
  return sig.hexdigest()

 def __api_call(self,method,params):
  self.__nonce()
  params['method'] = method
  params['nonce'] = str(self.__nonce_v)
  params = urllib.parse.urlencode(params)
  headers = {"Content-type" : "application/x-www-form-urlencoded",
                      "Key" : self.__api_key,
		     "Sign" : self.__signature(params)}
  conn = http.client.HTTPSConnection("btc-e.com")
  conn.request("POST", "/tapi", params, headers)
  response = conn.getresponse().read().decode()
  data = json.loads(response)
  conn.close()
  return data
