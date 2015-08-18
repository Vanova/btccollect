import urllib.request, urllib.parse, urllib.error
import http.client
# import simplejson as json
import json	 # replace w/ ujson or simplejson? (needs C binary)
import jsonfilter

############ Public API ##############
class pubapi():

 def connects(url, con_list):
  sconn = http.client.HTTPSConnection(url)
  jdata = []
  for path in range(len(con_list)):
   sconn.request("GET", con_list[path]['con'])
   response = sconn.getresponse().read().decode()
   jdata.append({'meth':con_list[path]['meth'],'pair':con_list[path]['pair'],'datas':json.loads(response)})
   print(url+con_list[path]['con'])
  jsonfilter.filters.jfstart(url, jdata)
  
  sconn.close()
  #end connects

 #trades
 def btce(url = "btc-e.com"):
  # limited to 15sec
  methods = ['ticker', 'depth']; # 'trades' (removing for now)
  pairs = ['btc_usd', 'eur_usd', 'btc_eur'];
  pairstring = "-".join(pairs)
  params = {"limit" : 2000, "ignore_invalid" : 1}
  url_values = urllib.parse.urlencode(params)
  con_list = []
  for meth in range(len(methods)):
   con_list.append({'meth':methods[meth], 'pair':pairs, 'con':"/api/3/%s" % methods[meth] + "/" + pairstring + "?" + url_values})
  pubapi.connects(url, con_list)

 def bitfinex(url = "api.bitfinex.com"):
  # ~1/sec
  methods = ['pubticker', 'book']; # 'trades' (removing for now)
  pairs = ['btcusd', 'drkusd', 'drkbtc'];
  params = {"limit_bids" : 2000, "limit_asks" : 2000}
  url_values = urllib.parse.urlencode(params)
  con_list = []
  for meth in range(len(methods)):
   for pair in range(len(pairs)):
    con_list.append({'meth':methods[meth], 'pair':pairs[pair], 'con':"/v1/%s" % methods[meth] + "/" + pairs[pair] + "?" + url_values})
  pubapi.connects(url, con_list)

 def btcchina(url = "data.btcchina.com"):
  # ~1/sec
  methods = ['orderbook', 'ticker']; # 'trades' (removing for now)
  pairs = ['btccny', 'ltccny', 'ltcbtc'];  # "ltccny", "btcltc"
  params = {"limit" : 5000}
  ob_values = urllib.parse.urlencode(params)
  tparams = {"limit" : 10000}
  trades_values = urllib.parse.urlencode(tparams)
  tlist = []
  for i in range(len(pairs)):tlist.append('ticker_'+pairs[i])
  con_list = []
  con_list.append({'meth':methods[1], 'pair':tlist, 'con':"/data/ticker?market=all"})
  for pair in range(len(pairs)):
   con_list.append({'meth':methods[0], 'pair':pairs[pair], 'con':"/data/%s" % methods[0] + "?market=" + pairs[pair] + "&" + ob_values})
  pubapi.connects(url, con_list)
 #end trades
  
###
## for testing
#pubapi.btce()
#pubapi.bitfinex()
#pubapi.btcchina()
