import os
import time
import hashlib
import requests
from bs4 import BeautifulSoup

def get_user_inputs():
    link = input("Enter URL of the desired webpage: ")
    token_id = input("Enter your Bot token id: ")
    user_id = input("Enter your chat id: ")
    api_token = input("Enter your Hugging Face API token: ")
    return link, token_id, user_id, api_token

def fetch_headlines(link):
    try:
        response = requests.get(link, timeout=10)
        response.raise_for_status()
        soup = BeautifulSoup(response.text, "html.parser")
        headlines = soup.find_all(["h1", "h2", "h3"])
        msg = list(dict.fromkeys([h.text.strip() for h in headlines if h.text.strip()]))  # Deduplicated
        head_text = " ".join(msg)
        return head_text, msg
    except Exception as e:
        print(f"❌ Error fetching webpage: {e}")
        return "", []

def summarize_text(api_token, head_text):
    url = "https://api-inference.huggingface.co/models/facebook/bart-large-cnn"
    headers = {
        "Authorization": f"Bearer {api_token}",
        "Content-Type": "application/json"
    }
    payload = {"inputs": head_text[:1024]}  # Limit to 1024 chars
    try:
        response = requests.post(url, headers=headers, json=payload, timeout=15)
        if response.status_code == 200:
            result = response.json()
            return result[0].get("summary_text", "Summary not available.")
        else:
            print("❌ Summarization failed:", response.status_code)
    except Exception as e:
        print("❌ Error during summarization:", str(e))
    return "Summary not available."

def send_telegram(token_id, user_id, message):
    url = f"https://api.telegram.org/bot{token_id}/sendMessage"
    data = {
        "chat_id": user_id,
        "text": message,
        "parse_mode": "Markdown"
    }
    try:
        response = requests.post(url, data=data, timeout=10)
        if response.status_code != 200:
            print("❌ Telegram send failed:", response.status_code)
    except Exception as e:
        print("❌ Error sending Telegram message:", e)

def check_and_notify(link, token_id, user_id, api_token):
    head_text, msg = fetch_headlines(link)
    if not head_text:
        print("⚠️ No headlines found or error occurred.")
        return

    current_hash = hashlib.sha256(head_text.encode()).hexdigest()
    hash_file = "final_hash.txt"
    headlines_file = "previous_headlines.txt"

    old_hash = ""
    if os.path.exists(hash_file):
        with open(hash_file, "r") as f:
            old_hash = f.read().strip()

    if old_hash == current_hash:
        print("✅ No changes detected.")
        return

    print("🔔 Content updated!")

    # Save new hash
    with open(hash_file, "w") as f:
        f.write(current_hash)

    # Load old headlines
    old_headlines = []
    if os.path.exists(headlines_file):
        with open(headlines_file, "r", encoding="utf-8") as f:
            old_headlines = f.read().splitlines()

    # Save current headlines
    with open(headlines_file, "w", encoding="utf-8") as f:
        f.write("\n".join(msg))

    # Detect new headlines
    new_headlines = [line for line in msg if line not in old_headlines]
    top_items = msg[:10] if not new_headlines else new_headlines[:10]

    # Get AI summary
    summary = summarize_text(api_token, head_text)

    # Format Telegram message
    message = (
        "🕵️‍♂️ *Webpage Update Detected!*\n\n"
        "🧠 *AI Summary:*\n"
        f"{summary}\n\n"
        "🗞️ *Headlines:*\n"
        + "\n".join([f"{i+1}. {line}" for i, line in enumerate(top_items)])
        + "\n\n📅 _Detected on: " + time.strftime('%d %b %Y, %I:%M %p') + "_"
    )

    # Send message
    send_telegram(token_id, user_id, message)

def main():
    link, token_id, user_id, api_token = get_user_inputs()
    check_and_notify(link, token_id, user_id, api_token)

if __name__ == "__main__":
    main()
