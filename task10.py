import json
from bs4 import BeautifulSoup
#from task5 import get_movie_list_details
with open ("webscrap5.json","r+") as f:
    a=json.load(f)
movie_list=a
def analyse_language_and_directors(movie_list):
    director_dic={}
    for movie in movie_list:
        for director in movie["director"]:
            #print(director)
            director_dic[director]={}
    for i in range(len(movie_list)):
        for director in director_dic:
            #print(director)
            if director in movie_list[i]["director"]:
                for movie in movie_list[i]["language"]:
                    #print(movie)
                    director_dic[director]["language"]=0
    for i in range(len(movie_list)):
        for director in director_dic:
            if director in movie_list[i]["director"]:
                for movie in movie_list[i]["language"]:
                    director_dic[director]["language"]+=1
        with open ("task10.json","w") as file10:
            json.dump(director_dic,file10,indent=4)
analyse_language_and_directors(movie_list)







            


