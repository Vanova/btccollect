from pymongo import MongoClient
import time

#################### VERY rough draft.. not working.

class filters():

## btce
# orderbook:
#	data[pair]["asks","bids"][n,n]
# trades:
#	data[pair]

 def btce(m,p,jd):
  for l in range(len(m)):
   for n in range(len(p)):
    print('btce: ', m[l], p[n])
    mongo.mdump('btce', m[l], p[n], jd)
   ## ?mongo.closeconnection()
  
 def bitfinex(m,p,jd):

 def btcchina(m,p,jd):

 def kraken(m,p,jd):

 def jfstart(url, meth, pair, jsdata):
  exchanges = {"btc-e.com":"btce",
			  "api.bitfinex.com":"bitfinex",
			  "data.btcchina.com":"btcchina",
			  "api.kraken.com":"kraken"}

  method = exchanges[url]
  if method=='btce':filters.btce(meth, pair, jsdata)
  if method=='bitfinex':filters.bitfinex(meth, pair, jsdata)
  if method=='btcchina':filters.btcchina(meth, pair, jsdata)
  if method=='kraken':filters.kraken(meth, pair, jsdata)

class mongo():

 ## Database.Collection
 def dbc(dbase,collection):
  db = client[dbase]  #client.dbase
  # db = client['test-database'] # dictionary access 
  coll = db[collection]  # collection = db['test-collection']
  print(coll)
  return coll

 def mdump(mpath, m, p, jd):
  mongo.dbc(mpath,m).insert_one(jd).inserted_id ###### DB.COLL.UTC[JDATA]
  print('To DB: ',mongo.dbc(mpath,m,p))
  
## Client Connection
# uri = "mongodb://myuser:mypass@sub.server.com:0000/mydb"
# client = MongoClient(uri) # uri connection option.
client = MongoClient('localhost', 27017) # standard connection



"""
## bitfindex

## btcchina

mdb.datacoll(self.__client,'btce','trades')
"""
"""
post = {"author": "Mike",
"text": "My first blog post!",
"tags": ["mongodb", "python", "pymongo"],
"date": datetime.datetime.utcnow()}

post_id = collection.insert_one(post).inserted_id
post_id

## List Collections
db.collection_names(include_system_collections=False)

"""
"""
>>> dct = {
...     "1": "a", 
...     "3": "b", 
...     "8": {
...         "12": "c", 
...         "25": "d"
...     }
... }
>>> 
>>> dct.keys()
['1', '8', '3']
>>> for key in dct.keys(): print key
...
1
8
3
>>>

If you need a sorted list:

keylist = dct.keys()
keylist.sort()
"""