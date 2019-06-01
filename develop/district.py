import urllib.request
import json
import pandas as pd
import pymongo
 
def getdata(url):

    data = urllib.request.urlopen(url).read()
    data1 = data[2:]
    output = json.loads(data1)

    return output


conn = 'mongodb://localhost:27017'
client = pymongo.MongoClient(conn)   
db = client.analysis
    
url = "https://www12.statcan.gc.ca/rest/census-recensement/CR2016Geo.json?lang=E&geos=FED&cpt=35"
collection = db.districts
collection.update({}, getdata(url), upsert=True) 
 

districts= client.db.districts
distlist = [] 

df = pd.DataFrame(list(districts.find()))
df.transpose


for rows in df['DATA']:
    for i in range(len(rows)):
        distlist.append(rows[i][0])
        print(rows[i][0])

        
        