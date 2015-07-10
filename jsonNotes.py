btce(method, pair, jsdata):
 for i in method:
  for p in pair:
   jsdata[p]=db.trade.method[i].time(UTC).pair[p]
 ## pair is json key

bitfinex(method, pair, jsdata):
 count=0
 for i in method:
  for p in pair:
   jsdata[count]=db.trade.method[i].time(UTC).pair[p]
   count+=1
 ## pair is pair[string]

btcchina(method, pair, jsdata):
 count=0
 for p in pair:
  jsdata[count]=db.trade."ticker".time(UTC).pair[p]
  count+=1
 for i in method:
  jsdata[count]=db.trade.method[i].time(UTC).pair[p]
  count+=1