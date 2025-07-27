import os 
import hashlib
import requests
from bs4 import BeautifulSoup   

link=input("Enter URL of the desired webpage:")
web_response=requests.get(link)
txt=web_response.text

docs=BeautifulSoup(txt,"html.parser")
headlines=docs.find_all(["h1","h2","h3","h4","h5","h6"]) 
head_text=""
for heads in headlines:
    head_text=head_text+heads.text
msg=[]
for lines in headlines:
    clean=lines.text
    msg.append(clean)
    msg.append("")

current_hash=hashlib.sha256(head_text.encode()).hexdigest()
hash_file="final_hash.txt"
if os.path.exists(hash_file):
    with open(hash_file, "r") as fp:
        old_files=fp.read()
else:
    old_files=""
if old_files != current_hash:
    print("Content Updated")
    with open(hash_file, "w") as fr:
        fr.write(current_hash)
        
    token_id="8246761969:AAE9sz-XfjtFw92C9eZRg0qRcFExMu6Zjdw"
    user_id="1264677922"
    message=f"Webpage Updated! \n\nTop Headlines:\n{head_text[:4000]}"
    url = f"https://api.telegram.org/bot{token_id}/sendMessage"
    data = {"chat_id": user_id, "text": message}
    telegram_response = requests.post(url, data=data)
else:
    print("No changes yet")



