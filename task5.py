import json
import requests
from bs4 import BeautifulSoup
from task1 import scrape_top_list
from task4 import scrape_movie_details

movie=scrape_top_list()
#print(movie)

def get_movie_list_details():
    movie_list=[]
    for i in movie:
        a=i["Url"]
        list_of_movies=scrape_movie_details(i["Name"],a)
        movie_list.append(list_of_movies)
        print(movie_list)
    with open("webscrap5.json","w") as file5:
        json.dump(movie_list,file5,indent=4)
get_movie_list_details()

