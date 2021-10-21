import json
import requests
from bs4 import BeautifulSoup
with open("webscrap5.json","r") as f:
    data=json.load(f)
def analysis_movie_director():
    director_dic={}
    for i in data:
        data1=i["director"]
        for director in data1:
            if director not in director_dic:
                data1=i["director"]
                director_dic[director]=1
            else:
                director_dic[director]+=1
    with open ("task7.json","w") as file7:
        json.dump(director_dic,file7,indent=4)
analysis_movie_director()
    

    




