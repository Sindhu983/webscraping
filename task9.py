import requests
import json
import os
import time
import random

with open('webscrap5.json','r+') as f:
    a=json.load(f)
movies_data=a
# print(movies_data)
def moviedata(movies_data):
    for i in movies_data:
            random_sleep=random.randint(1,3)
            path=open("/home/admin123/web_scraping/9.text"+i["movieName"]+".txt",'w+')
            a=str(i)
            create=path.write(a)
            time.sleep(random_sleep)
            path.close()
moviedata(movies_data)