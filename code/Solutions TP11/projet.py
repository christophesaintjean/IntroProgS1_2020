import codecs
import json

with codecs.open("projet.json", "r", "utf-8") as f:
     data = json.load(f)    
    
def nb_fromages(data):
    return len(data)

def nb_attribs(data):
    return len(data[0])


print(nb_fromages(data))
print(nb_attribs(data))

