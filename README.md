# btccollect
Collects Public API Information from various BTC Exchanges and pushes to a mongoDB

Needed:
  - JSON data needs to be formatted the same way for all exchanges before entering the db (jsonfilter)
  - Private API: Create Order objects and link to mongo via ID. Set secondary attributes and store (See Flow Diagram)
  - Implement Logging
  - Error Management
  - Replace urllib with requests?

Planned:
  - JSON Comparison for new db objects (trades, ob values, assign start and endtime rather than placing the entry in multiple times. to help with db size)
  - Numpy/Pandas and Monary integration for DataFrames
  - WebSocket (Tornado?)
  - Graphing?
  
If you happen to stumble on this project, I would love some advice/suggestions!
