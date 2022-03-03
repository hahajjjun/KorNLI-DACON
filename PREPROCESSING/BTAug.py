'''
BTAug.py is KR>EN>KR back-translation module.
Based on Selenium. Hongsun Jang
https://github.com/hongsunjang/dacon_koreaNLI/blob/main/augmentation/back_translation.py
'''
import pandas as pd 
import selenium 
from selenium import webdriver 
from bs4 import BeautifulSoup 
import time 
from tqdm import tnrange 
from urllib.request import urlopen 
import re 
import requests 
import urllib.request 
from tqdm import tqdm
import csv

train = pd.read_csv('data/benchmark_train_data.csv') 
test = pd.read_csv('data/test_data.csv')


train_premise = train['premise']
train_hypothesis = train['hypothesis']

test_premise = test['premise']
test_hypothesis = test['hypothesis']


trans_list = [] 
backtrans_list = []


driver = webdriver.Chrome(executable_path='/usr/local/share/chromedriver') 
driver.maximize_window()

def kor_to_trans(text_data, trans_lang): 
    """ trans_lang에 넣는 파라미터 값: 'en' -> 영어 'ja&hn=0' -> 일본어 'zh-CN' -> 중국어(간체) """ 
    for i in tqdm(range(len(text_data))):
        try: 
            driver.get('https://papago.naver.com/?sk=ko&tk='+trans_lang+'&st='+text_data[i]) 
            time.sleep(4) 
            backtrans = driver.find_element_by_xpath('//*[@id="txtTarget"]').text 
            trans_list.append(backtrans)
        except: 
            driver.get('https://papago.naver.com/?sk=ko&tk='+trans_lang) 
            time.sleep(4)
            driver.find_element_by_xpath('//*[@id="txtSource"]').send_keys(text_data[i]) 
            time.sleep(4)
            backtrans = driver.find_element_by_xpath('//*[@id="txtTarget"]').text 
            trans_list.append(backtrans) 

def trans_to_kor(transed_list, transed_lang):
     for i in tqdm(range(len(transed_list))):
        try: 
            driver.get('https://papago.naver.com/?sk='+transed_lang+'&tk=ko&st='+transed_list[i]) 
            time.sleep(4) 
            backtrans = driver.find_element_by_xpath('//*[@id="txtTarget"]').text 
            backtrans_list.append(backtrans) 
        except: 
            driver.get('https://papago.naver.com/?sk='+transed_lang+'&tk=ko') 
            time.sleep(4) 
            driver.find_element_by_xpath('//*[@id="txtSource"]').send_keys(transed_list[i]) 
            time.sleep(4) 
            backtrans = driver.find_element_by_xpath('//*[@id="txtTarget"]').text 
            backtrans_list.append(backtrans)

# TRAIN
kor_to_trans(train_premise[:10000], 'en')
trans_to_kor(trans_list, 'en')


df = pd.DataFrame({'premise': backtrans_list})
df.to_csv('train_premise_0.csv')
trans_list = [] 
backtrans_list = []

kor_to_trans(train_hypothesis[:10000], 'en')
trans_to_kor(trans_list, 'en')


df = pd.DataFrame({'hypothesis': backtrans_list})
df.to_csv('train_hypothesis_0.csv')
trans_list = [] 
backtrans_list = []

"""
kor_to_trans(train_premise[10000:20000], 'en')
trans_to_kor(trans_list, 'en')
df = pd.DataFrame({'premise': backtrans_list})
df.to_csv('train_premise_1.csv')
trans_list = [] 
backtrans_list = []
kor_to_trans(train_hypothesis[10000:20000], 'en')
trans_to_kor(trans_list, 'en')
df = pd.DataFrame({'hypothesis': backtrans_list})
df.to_csv('train_hypothesis_1.csv')
trans_list = [] 
backtrans_list = []
"""


# TEST
"""
kor_to_trans(test_premise, 'en')
trans_to_kor(trans_list, 'en')
df = pd.DataFrame({'premise': backtrans_list})
df.to_csv('test_premise.csv')
trans_list = [] 
backtrans_list = []
kor_to_trans(test_hypothesis, 'en')
trans_to_kor(trans_list, 'en')
df = pd.DataFrame({'hypothesis': backtrans_list})
df.to_csv('train_hypothesis.csv')
"""

driver.close()