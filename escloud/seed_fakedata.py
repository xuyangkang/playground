import csv
import numpy as np
import json
from elasticsearch import Elasticsearch


username1 = ''
password1 = ''
# e9752b: 2 nodes
with open('credentials-e9752b-2021-Jun-10--10_30_30.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        username1, password1 = row

username2 = ''
password2 = ''
# f319a3: 1 node
with open('credentials-f319a3-2021-Jun-10--10_31_54.csv') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        username2, password2 = row


client1 = Elasticsearch(f'https://{username1}:{password1}@i-o-optimized-deployment-e9752b.es.ap-northeast-1.aws.found.io:9243')
client2 = Elasticsearch(f'https://{username2}:{password2}@i-o-optimized-deployment-f319a3.es.ap-northeast-1.aws.found.io:9243')
print(client1.cluster.health())
print(client2.cluster.health())

def bulk_upsert(es_client, companies):
    flat_chunk = []
    if not companies:
        return
    for company in companies:
        action = "index"
        doc = json.dumps(company)
        flat_chunk.append(json.dumps({action: {"_id": int(company["code"])}}))
        flat_chunk.append(doc)

    body = "\n".join(flat_chunk)
    es_client.bulk(body, index='company', request_timeout=60)


for i in range(800):
    block = np.random.rand(1000,256)
    docs = []
    for j in range(1000):
        doc = {
            'code': i * 1000 + j,
            'vector': block[0].tolist()
        }
        docs.append(doc)
    bulk_upsert(client1, docs)
    bulk_upsert(client2, docs)
