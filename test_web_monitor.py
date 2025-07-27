#This is just a test version!
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
current_hash=hashlib.sha256(head_text.encode()).hexdigest()#generate a hash file for the extracted headlines
hash_file="final_hash.txt"
if os.path.exists(hash_file):
    with open(hash_file, "r" )as fp:
        old_files=fp.read()#read the old hash from the stored file 
else:
    old_files=""
if old_files != current_hash:#compare the old hash and the new hash files
    print("Content Updated")
    with open(hash_file, "w")as fr:
        fr.write(current_hash)#update the hash 
        
    token_id="Your BOT TOKEN "
    user_id="Your Telegram Chat ID"
    message="Theres an update!!"
    url = f"https://api.telegram.org/bot{token_id}/sendMessage"#send the message using telegram API
    data = {"chat_id": user_id, "text": message}
    telegram_response = requests.post(url, data=data)
else:
    print("No changes yet ")
        





