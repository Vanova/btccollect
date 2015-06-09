import urllib.request, urllib.parse, urllib.error
import http.client
# import simplejson as json    
import json			# replace w/ ujson or simplejson? (C binary)
import pprint
import jsonfilter  # filter class. work in progress

class pubapi():

	def connects(conn, path, meth, pair):
	 sconn = http.client.HTTPSConnection(conn)
	 sconn.request("GET", path)
	 print(conn+path)
	 response = sconn.getresponse().read().decode()
	 jsdata = json.loads(response)

	 if isinstance(pair, list):
	  for n in range(len(pair)):
	   # jsonfilter.filters.jfstart(conn,meth,pair[n],jsdata)
	 else:
	  # jsonfilter.filters.jfstart(conn,meth,pair,jsdata)

	 sconn.close()
	 #end connects

	def btce(url = "btc-e.com"):
	 # limited to ~15sec
	 methods = ['ticker', 'depth', 'trades'];
	 pairs = ['btc_usd', 'eur_usd', 'btc_eur'];
	 pairstring = "-".join(pairs)
	 params = {"limit" : 2000, "ignore_invalid" : 1}
	 url_values = urllib.parse.urlencode(params)

	 for meth in range(len(methods)):
	  path = "/api/3/%s" % methods[meth] + "/" + pairstring + "?" + url_values
	  pubapi.connects(url, path, methods[meth], pairs)

	def bitfinex(url = "api.bitfinex.com"):
	 ## ~1/sec
	 ## https://api.bitfinex.com/v1/pubticker/btcusd
	 ## btcusd, ltcusd, ltcbtc, drkusd, drkbtc
	 methods = ['pubticker', 'book', 'trades'];
	 pairs = ['btcusd', 'drkusd', 'drkbtc'];
	 params = {"limit_bids" : 2000, "limit_asks" : 2000}
	 url_values = urllib.parse.urlencode(params)

	 for meth in range(len(methods)):
	  for pair in range(len(pairs)):
	   path = "/v1/%s" % methods[meth] + "/" + pairs[pair] + "?" + url_values
	   pubapi.connects(url, path, methods[meth], pairs[pair])

	def btcchina(url = "data.btcchina.com"):
	 ## ~1/sec
	 ## https://data.btcchina.com/data/orderbook?market=btccny&limit=5000
	 ## market=all (ticker only?)
	 ## limit=10000 (trades)	 ## limit=5000 ask/bid
	 ## btccny, ltccny, btcltc
	 methods = ['orderbook', 'trades'];
	 pairs = ['btccny', 'ltccny', 'btcltc'];  ## , "ltccny", "btcltc"
	 params = {"limit" : 5000}
	 ob_values = urllib.parse.urlencode(params)
	 tparams = {"limit" : 10000}
	 trades_values = urllib.parse.urlencode(tparams)
	 ## Ticker (breaks filter)
	 #pubapi.connects(url, "/data/ticker?market=all", "ticker", ("ticker_" for n in range(len(pairs))))

	 for pair in range(len(pairs)):
	  path = "/data/%s" % methods[0] + "?market=" + pairs[pair] + "&" + ob_values
	  pubapi.connects(url, path, methods[0], pairs[pair])
	  path = "/data/%s" % methods[1] + "?market=" + pairs[pair] + "&" + trades_values
	  pubapi.connects(url, path, methods[1], pairs[pair])

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
####

## for testing
#pubapi.btce()
#pubapi.bitfinex()
#pubapi.btcchina()
#pubapi.kraken()
