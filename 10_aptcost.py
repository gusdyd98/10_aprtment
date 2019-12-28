#print("hello python!")
#-*- coding:utf-8 -*-
from urllib.request import urlopen
import json
import csv

baseURL1 = "http://apis.data.go.kr/1611000/AptListService/getLegaldongAptList?loadCode="
baseURL2 = "&_type=json&numOfRows=100&ServiceKey=6fC%2FE%2FOfXdNsSQPKEtWOgorYlxR7czIHUrRj8f6waylgRRJuo7qajzbZCz2Yn959nXz6bWMcDmS1vJG%2BJjk3tQ%3D%3D"
with open('data/kyunggi.csv', 'rt', encoding='utf-8') as csvfile:
    rows=csv.reader(csvfile, delimiter='\t')
    for r in rows:
        print(r[1])
        url=baseURL1+r[0]+baseURL2
        page=urlopen(url)
        response = page.read().decode('utf8')
        decoded=json.loads(response)
        #print(decoded)
        if decoded['response']['header']['resultCode']!="00":
            print('querry error')
            exit(1)
        total=decoded['response']['body']['totalCount']
        if total==0 or decoded['response']['body']['items']=="":
            continue
        elif isinstance(decoded['response']['body']['items']['item'],dict):
            print(decoded['response']['body']['items']['item']['kaptCode']+""+decoded['response']['body']['items']['item']['kaptName'])
        elif isinstance(decoded['response']['body']['items']['item'], list):
            for item in decoded['response']['body']['items']['item']:
                print(item['kaptCode']+" "+item['kaptName'])

