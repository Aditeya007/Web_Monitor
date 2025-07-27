import os
import requests
from bs4 import BeautifulSoup
import hashlib

#fetching content from the web 
web_response=requests.get("https://spiderman.fandom.com/wiki/Spider-Man_Wiki")
txt=web_response.text 
docs=BeautifulSoup(txt,"html.parser")#parse the HTML content into a simple structure 
headlines=docs.find_all(["h1","h2"])#collect the headlines
head_text=""
for heads in headlines:
    head_text=head_text+heads.text



