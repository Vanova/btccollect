from pymongo import MongoClient
import time

#################### VERY rough draft.. not working.

class filters():

 def btce(m,p,jd):
  stamp=time.time()
  for l in range(len(m)):
   print('btce: ', m[l], p)
   mongo.mdump('btce', m[l], stamp, jd)

 def bitfinex(m,p,jd):
  stamp=time.time()
  count=0
  for l in range(len(m)):
   for n in range(len(p)):
    print('btce: ', m[l], p[count])
    mongo.mdump('btce', m[l], stamp, p[count], jd)
    count+=1

 def btcchina(m,p,jd):
  stamp=time.time()
  count=0
  for l in range(len(m)):
   for n in range(len(p)):
    print('btce: ', m[l], p[count])
    mongo.mdump('btce', m[l], stamp, p[count], jd)
    count+=1

 def kraken(m,p,jd):
  stamp=time.time()
  count=0
  for l in range(len(m)):
   for n in range(len(p)):
    print('btce: ', m[l], p[count])
    mongo.mdump('btce', m[l], stamp, p[count], jd)
    count+=1

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

 def mdump(mpath, m, stamp, p*, jd):
  if p:
   mongo.dbc(mpath,m).insert_one({stamp:{p:{{jd}}}).inserted_id
   print('To DB: ',mongo.dbc(mpath,m),p,stamp)
  mongo.dbc(mpath,m).insert_one({stamp:{jd}}).inserted_id
  print('To DB: ',mongo.dbc(mpath,m),stamp)
  
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
