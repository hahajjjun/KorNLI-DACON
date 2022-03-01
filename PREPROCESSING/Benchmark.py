'''
Benchmark.py : Benchmarking additional dataset(KLUE Dev set).
KLUE Dev set is JSON format, thus reformatting into csv is required.
'''

##### IMPORT #####
import pandas as pd
import json
from tqdm import tqdm

##### LOAD DATA #####
TRAIN = '/content/drive/MyDrive/DACON_MONTHLYNLI/train_data.csv'
TEST = '/content/drive/MyDrive/DACON_MONTHLYNLI/test_data.csv'
KLUE_TRAIN = '/content/drive/MyDrive/DACON_MONTHLYNLI/klue-nli-v1.1_train.json'
KLUE_DEV = '/content/drive/MyDrive/DACON_MONTHLYNLI/klue-nli-v1.1_dev.json'
train = pd.read_csv(TRAIN)
test = pd.read_csv(TEST)
with open(KLUE_TRAIN, "r") as train_json:
  klue_train = json.load(train_json)
with open(KLUE_DEV, "r") as dev_json:
  klue_dev = json.load(dev_json)

##### CONCATENATE AND REINDEXING #####
new_train = {'premise':[], 'hypothesis':[], 'label':[]}
new_dev = {'premise':[], 'hypothesis':[], 'label':[]}

for idx, data in enumerate(klue_train):
  new_train['premise'].append(data['premise'])
  new_train['hypothesis'].append(data['hypothesis'])
  new_train['label'].append(data['gold_label'])

for idx, dev_data in enumerate(klue_dev):
  new_dev['premise'].append(dev_data['premise'])
  new_dev['hypothesis'].append(dev_data['hypothesis'])
  new_dev['label'].append(dev_data['gold_label'])
  
new_train_df = pd.DataFrame(new_train)
new_dev_df = pd.DataFrame(new_dev)
train = train.drop('index', axis = 1)
train = pd.concat([train, new_dev_df])
train = train.reset_index()
train = train.drop('index', axis =1)
train = train.reset_index()
train.to_csv('benchmark_train_data.csv', index = False)