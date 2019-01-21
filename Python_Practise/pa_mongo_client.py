import pymongo

uri = "mongodb://kugou_admin:Xiaoxian0910@techinfo.xin:27017"
client = pymongo.MongoClient(uri)
db = client['kugou']
collection = db['kugoump3']

for n in collection.find():
    print(n.get('name'))