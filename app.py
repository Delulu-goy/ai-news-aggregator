from flask import Flask, render_template
import feedparser
from datetime import datetime

app = Flask(__name__)

RSS_FEEDS = {
    "TechCrunch AI": "https://techcrunch.com/category/artificial-intelligence/feed/",
    "VentureBeat AI": "https://venturebeat.com/category/ai/feed/",
    "MIT Technology Review AI": "https://www.technologyreview.com/feed/topic/artificial-intelligence/",
    "OpenAI Blog": "https://openai.com/blog/rss.xml",
    "Google AI Blog": "https://blog.google/technology/ai/rss",
    "Anthropic Blog": "https://www.anthropic.com/rss",
    "Hugging Face Blog": "https://huggingface.co/blog/rss.xml"
}

ARTICLES_PER_SOURCE = 4

def parse_date(date_str):
    if not date_str:
        return ""
    try:
        dt = datetime(*date_str[:6])
        return dt.strftime("%b %d, %Y")
    except:
        return date_str[:16] if len(date_str) > 16 else date_str

def fetch_feed(source_name, url):
    try:
        feed = feedparser.parse(url)
        articles = []
        for entry in feed.entries[:ARTICLES_PER_SOURCE]:
            article = {
                "title": entry.get("title", "Untitled"),
                "link": entry.get("link", "#"),
                "date": parse_date(entry.get("published_parsed"))
            }
            articles.append(article)
        return {"name": source_name, "articles": articles, "error": None}
    except Exception as e:
        return {"name": source_name, "articles": [], "error": str(e)}

@app.route("/")
def index():
    news_sources = []
    for source_name, url in RSS_FEEDS.items():
        news_sources.append(fetch_feed(source_name, url))
    
    last_updated = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    return render_template("index.html", sources=news_sources, last_updated=last_updated)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
