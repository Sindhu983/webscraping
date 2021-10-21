import requests
from bs4 import BeautifulSoup
from task1 import scrape_top_list
import os
movie=scrape_top_list()
def scrap_movie_details():
    for i in movie:
        page=("/home/admin123/web_scraping/task2.py")+i["Name"]+".text"
        if os.path.exist(page):
            pass
        else:
            data=open("/home/admin123/web_scraping/t.text"+i["Name"]+".text","w")
            url=requests.get(i["Url"])
            create=data.write(url.text)
            data.close()
scrap_movie_details()