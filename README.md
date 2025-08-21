# 🕵️‍♂️ Webpage Monitor

A Python-based intelligent webpage monitoring tool that tracks content changes and sends instant notifications to your Telegram chat with AI-powered summaries.

## ✨ Features

- **Real-time Monitoring**: Continuously monitors any webpage for content changes
- **Smart Change Detection**: Uses SHA-256 hashing to detect even minor content modifications
- **AI-Powered Summaries**: Leverages Hugging Face's BART model for intelligent content summarization
- **Telegram Integration**: Instant notifications sent directly to your Telegram chat
- **Headline Tracking**: Extracts and tracks H1, H2, and H3 headlines from webpages
- **Flexible Scheduling**: Customizable monitoring duration and check intervals
- **Persistent Storage**: Maintains history of previous content for comparison
- **User-Friendly Interface**: Interactive command-line prompts for easy setup

## 🚀 Quick Start

### Prerequisites

- Python 3.6 or higher
- Internet connection
- Telegram Bot Token
- Hugging Face API Token

### Installation

1. **Clone or download this script**
```bash
git clone <repository-url>
cd webpage-monitor
```

2. **Install required dependencies**
```bash
pip install requests beautifulsoup4
```

3. **Run the script**
```bash
python webpage_monitor.py
```

## 🔧 Setup Guide

### 1. Create a Telegram Bot

1. Open Telegram and search for `@BotFather`
2. Send `/newbot` command
3. Follow the instructions to create your bot
4. Copy the **Bot Token** (format: `123456789:ABCdefGHIjklMNOpqrsTUVwxyz`)

### 2. Get Your Chat ID

1. Send a message to your bot
2. Visit: `https://api.telegram.org/bot<YOUR_BOT_TOKEN>/getUpdates`
3. Look for `"chat":{"id":XXXXXXXXX}` - this is your **Chat ID**

### 3. Get Hugging Face API Token

1. Visit [Hugging Face](https://huggingface.co/)
2. Create an account and go to Settings → Access Tokens
3. Create a new token with "Read" permissions
4. Copy your **API Token**

### 4. Run the Monitor

Execute the script and provide the required information:

```
Enter URL of the desired webpage: https://example.com
Enter your Bot token id: 123456789:ABCdefGHIjklMNOpqrsTUVwxyz
Enter your chat id: 987654321
Enter your Hugging Face API token: hf_xxxxxxxxxxxxxxxxxxxxxxxxx
⏱ Enter total monitoring duration (in minutes): 60
🔁 Enter check interval (in minutes): 5
```

## 📋 How It Works

1. **Content Extraction**: Scrapes the target webpage and extracts all H1, H2, and H3 headlines
2. **Change Detection**: Creates a SHA-256 hash of the content to detect any modifications
3. **Comparison**: Compares current content with previously stored data
4. **AI Analysis**: If changes are detected, generates an intelligent summary using BART-large-CNN
5. **Notification**: Sends formatted update to your Telegram chat with:
   - AI-generated summary
   - New or updated headlines
   - Timestamp of detection

## 📱 Telegram Notifications

### When No Changes Are Detected:
```
✅ No content changes detected.
🕰️ Checked at: 22 Aug 2025, 02:30 PM
```

### When Changes Are Found:
```
🕵️‍♂️ Webpage Update Detected!

🧠 AI Summary:
Breaking news about technology updates and market changes affecting global industries...

🗞️ Headlines:
1. Major Tech Company Announces New Product
2. Market Sees Significant Growth
3. Industry Leaders Meet for Summit

📅 Detected on: 22 Aug 2025, 02:35 PM
```

## 📁 Generated Files

The script creates two files in the same directory:

- `final_hash.txt`: Stores the SHA-256 hash of the last checked content
- `previous_headlines.txt`: Contains the headlines from the previous check

## ⚙️ Configuration Options

| Parameter | Description | Example |
|-----------|-------------|---------|
| URL | Target webpage to monitor | `https://news.example.com` |
| Bot Token | Telegram bot authentication | `123456789:ABC...` |
| Chat ID | Your Telegram chat identifier | `987654321` |
| API Token | Hugging Face API access token | `hf_xxx...` |
| Duration | Total monitoring time (minutes) | `60` |
| Interval | Check frequency (minutes) | `5` |

## 🛡️ Error Handling

The script includes robust error handling for:

- Network connectivity issues
- Invalid webpage responses
- Telegram API failures
- Hugging Face API timeouts
- File I/O operations
- User input validation

## 🔒 Security Considerations

- **API Tokens**: Never share your bot token or API keys
- **Rate Limits**: Respects API rate limits to avoid service disruption
- **User Agent**: Uses proper headers to avoid being blocked by websites
- **Timeout Handling**: Implements timeouts for all network requests

## 💡 Use Cases

- **News Monitoring**: Track breaking news on your favorite news sites
- **Product Updates**: Monitor product pages for new releases or price changes
- **Blog Watching**: Stay updated with your favorite blogs and publications
- **Competitor Analysis**: Track competitor website changes
- **Content Publishing**: Monitor when new content is published on specific sites

## 🐛 Troubleshooting

### Common Issues:

**Bot not responding?**
- Verify your bot token is correct
- Make sure you've sent at least one message to your bot first

**No content detected?**
- Check if the webpage has H1, H2, or H3 tags
- Verify the URL is accessible and doesn't require authentication

**Summarization failing?**
- Ensure your Hugging Face token has proper permissions
- Check if the API service is available

**Script stops unexpectedly?**
- Check your internet connection
- Verify all tokens and IDs are correct



## 📄 License

This project is open source. Feel free to modify and distribute according to your needs.

---

**Happy Monitoring! 🎉**

*Stay informed without constantly checking websites manually.*
