from pymongo import MongoClient

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
    print('btce: ',m[l],' ',p[n])
  #mongo.mdump('btce', m, p, jd) Needs a good way to sort data in db.
  
 def bitfinex(m,p,jd):
  for l in range(len(m)):
   for n in range(len(p)):
    print('bitfinex: ',m[l],' ',p[n])

 def btcchina(m,p,jd):
  for l in range(len(m)):
   for n in range(len(p)):
    print('btcchina: ',m[l],' ',p[n])

 def kraken(m,p,jd):
  for l in range(len(m)):
   for n in range(len(p)):
    print('kraken: ',m[l],' ',p[n])

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
  if len(m)+len(p)>len(jd):
   for l in range(len(m)):
    for n in range(len(p)): ######### l -> method set
	 
     mongo.dbc(mpath,m[l]).insert_one(jd[l]).inserted_id
     print('To DB: ',mongo.dbc(mpath,m[l]))
  else:
   for l in range(len(m)):
    for n in range(len(p)): ######### l -> method set
     mongo.dbc(mpath,m[l]).insert_one(jd[l+n]).inserted_id
     print('To DB: ',mongo.dbc(mpath,m[l]))
  
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