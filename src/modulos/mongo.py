# Mongodb
from pymongo import MongoClient

# Mongo URL Atlas
MONGO_URL_ATLAS = 'mongodb+srv://enmodoflow:root@cluster0-9tze7.mongodb.net/test?retryWrites=true&w=majority'

client = MongoClient(MONGO_URL_ATLAS, ssl_cert_reqs=False)
db = client['sorteo']
collection = db['sorteo']

