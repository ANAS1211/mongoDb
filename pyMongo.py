from pymongo import MongoClient
#connecter le port 27017 de la machine 
# locale au port 27017 du conteneur
client = MongoClient(
    host="127.0.0.1",
    port = 27017
)
print(client.list_database_names()) #equivalent à show dbs command

#mongoimport -d sample -c zips --file /data/db/zips.json
#selection la base de données sample
sample = client["sample"]
#selection de la collection zips
c_zips = sample["zips"]
# we can write like this also 
# c_zips = client["sample"]["zips"]

print(list(c_zips.find_one()))

#créer une collection nommée "rand"
rand = sample.create_collection(name="rand")

# We can check the creation of the collection with this 
print(sample.list_collection_names())

#insérer des documents
data = [
  {"name": "Melthouse","bread":"Wheat","sauce": "Ceasar"},
  {"name": "Italian BMT", "extras": ["pickles","onions","lettuce"],"sauce":["Chipotle", "Aioli"]},
  {"name": "Steakhouse Melt","bread":"Parmesan Oregano"}, 
  {"name": "Germinal", "author":"Emile Zola"}, 
  {"pastry":"cream puff","flavour":"chocolate","size":"big"}
]

rand.insert_many(data)

zips = client["sample"]["zips"]
#projections avec la fonction find. 
# Récupérons la clé city des documents de la collection zips :
for i in list(zips.find({},{"_id":0,"city":1})):
    print(i)