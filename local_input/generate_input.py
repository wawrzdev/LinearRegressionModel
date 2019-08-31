#Generate Input
#generates 100 csv input streams of 1000 entries with values that are in the range of the known dataset

#imports
from sklearn.datasets import load_boston
import pandas as pd
import random
import csv, io, json

data_set = load_boston()
boston = pd.DataFrame(data_set.data, columns=data_set.feature_names)

for i in range(100) :
    name = "Input/input" + str(i) + ".json"
    f = open(name, "w+")
    string = "LSTAT,TAX,ZN,RM\n"
    for j in range(1000) :
        rand1 = random.uniform(min(boston['LSTAT']), max(boston['LSTAT']) + 1)
        rand2 = random.uniform(min(boston['TAX']), max(boston['TAX']) + 1)
        rand3 = random.uniform(min(boston['ZN']), max(boston['ZN']) + 1)
        rand4 = random.uniform(min(boston['RM']), max(boston['RM']) + 1)
        string += str(rand1) + ',' + str(rand2) + ',' + str(rand3) + ',' + str(rand4) + '\n'
    reader = csv.DictReader(io.StringIO(string))
    json_data = json.dumps(list(reader))
    print(json_data)
    f.write(json_data)
