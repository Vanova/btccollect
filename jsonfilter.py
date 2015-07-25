from pymongo import MongoClient
import time

#################### VERY rough draft.
## To Do: global timestamp init, open mongo on method - close at end

class filters():
 ## data setup
 
 def btce(db,jd):
  stamp = str(time.time())
  datas = {}
  for l in range(len(jd)): # best way to create keys?
   datas.update({jd[l]['meth']:{}})
  for i in range(len(jd)):
   for p in jd[i]['pair']:
    datas[jd[i]['meth']].update({p:jd[i]['datas'][p]})
  for m in datas.keys():
   datas[m].update({'time':stamp})
   mongo.dbc(db,m).insert_one(datas[m]).inserted_id

 def bitfinex(db,jd):
  stamp = str(time.time())
  datas = {}
  for l in range(len(jd)): # best way to create keys?
   datas.update({jd[l]['meth']:{}})
  for i in range(len(jd)):
   datas[jd[i]['meth']].update({jd[i]['pair']:jd[i]['datas']})
  for m in datas.keys():
   datas[m].update({'time':stamp})
   mongo.dbc(db,m).insert_one(datas[m]).inserted_id
	
 def btcchina(db,jd):
  stamp = str(time.time())
  datas = {}
  for l in range(len(jd)): # best way to create keys?
   datas.update({jd[l]['meth']:{}})
  for i in range(len(jd)):
   if jd[i]['meth']=='ticker':
    for p in jd[i]['pair']:
     datas[jd[i]['meth']].update({p:jd[i]['datas'][p]})
   else:
    datas[jd[i]['meth']].update({jd[i]['pair']:jd[i]['datas']})  
  for m in datas.keys():
   datas[m].update({'time':stamp})
   mongo.dbc(db,m).insert_one(datas[m]).inserted_id

 def jfstart(url, jdata):
  exchanges = {'btc-e.com':'btce',
						'api.bitfinex.com':'bitfinex',
						'data.btcchina.com':'btcchina',
						'api.kraken.com':'kraken'}
  
  if exchanges[url]=='btce':filters.btce(exchanges[url], jdata)
  if exchanges[url]=='bitfinex':filters.bitfinex(exchanges[url], jdata)
  if exchanges[url]=='btcchina':filters.btcchina(exchanges[url], jdata)

class mongo():
 ## Database.Collection
 def dbc(dbase,collection):
  # uri = "mongodb://myuser:mypass@sub.server.com:0000/mydb"
  # client = MongoClient(uri) # uri connection option.
  client = MongoClient('localhost', 27017) # standard connection
  
  db = client[dbase] #client.dbase / db = client['test-database'] - dictionary access  /  Labled as trade
  coll = db[collection]  # collection = db['test-collection']  /  Labled as method
  print('DBACCESS: ', coll)
  return coll

'''
 def mdump(mpath, m, stamp, jd, p):
  print(type(p), len(p))
  data = {}
  if type(p) is list:
   for n in range(len(p)):
    data.update({p[n]:jd[p[n]]})
   data.update({'time':stamp})
   mongo.dbc(mpath,m).insert_one(data).inserted_id
   print('DATAS: ', p, data)
  else:
   data.update({'time':stamp})
   data.update(jd[p])
   mongo.dbc(mpath,m).insert_one(data).inserted_id
   print('DATAS: ', p, data)
'''


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