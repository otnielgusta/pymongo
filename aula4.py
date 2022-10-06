import json

from pymongo import MongoClient
from bson import ObjectId
client = MongoClient("localhost", 27017)

#prepara a criação da base de dados
db = client.Aula4

#inserir um registro
# db.pessoas.insert_one({
#     "_id": ObjectId(),
#     "Nome": "Juquinha",
#     "idade": 45,
#     "endereco": ObjectId('6328a173accc211326205987')
# })

# db.pessoas.insert_one({
#     "id": 1,
#     "Nome": "Juquinha",
#     "idade": 45,
#     "filhos": ["Juninho", "Pedrinho", "Zé capivara"]
# })

# db.endereco.insert_one({
#     "id": 1,
#     "Nome": "Rua tal",
#     "Numero": 45,
# })

pessoa = list(db.pessoas.aggregate([
    {"$match": {"_id": ObjectId('6329c918f64692451c70ebc0')}},
        {"$lookup":
        {
            "from": "endereco",
            "localField": "endereco",
            "foreignField": "_id",
            "as": "endereco"
        }
}]))

for chave, valor in pessoa[0].items():
    print(chave, " => ", valor)