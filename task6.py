
import json

with open("webscrap5.json","r") as f:
     movie=json.load(f)
def analyse_movie_language(movie):
    language_dic={}
    for i in movie:
        if "language" in i:
            language=i["language"]
            if language not in language_dic:
                language=i["language"]
                language_dic[language]=1
            else:
                language_dic[language] += 1
        else:
            continue

    with open ("webscrap6.json","w") as file6:
        json.dump(language_dic,file6,indent=4)
        # print(language_dic)
analyse_movie_language(movie)


