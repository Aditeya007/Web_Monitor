import os 
import hashlib
import requests
from bs4 import BeautifulSoup   

link=input("Enter URL of the desired webpage:")
token_id=input("Enter your Bot token id")
user_id=input("Enter your chat id")

api_token=input("Enter your API token !")
url="https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
headers={"Authorization":f"Bearer {api_token}",
         "Content-Type":"application/json"
         }

web_response=requests.get(link)
txt=web_response.text

docs=BeautifulSoup(txt,"html.parser")
headlines=docs.find_all(["h1","h2","h3"]) 
head_text=""
for heads in headlines:
    head_text=head_text+heads.text
payload = {
    "inputs": head_text
}
summary = "Summary not available."
try:
    response = requests.post(url, headers=headers, json=payload)
    if response.status_code == 200:
        result = response.json()
        summary = result[0]["summary_text"]
    else:
         print(" Summarization failed:", response.status_code)
except Exception as e:
    print("Error during summarization:", str(e))

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

    formatted_msg = "\n".join(msg)
    message = f"Webpage Updated!\n\n AI Summary:\n{summary}\n\nHeadlines:\n{formatted_msg[:4000]}"
    tele_url = f"https://api.telegram.org/bot{token_id}/sendMessage"
    data = {"chat_id": user_id, "text": message}
    telegram_response = requests.post(tele_url, data=data)
else:
    print("No changes yet")



