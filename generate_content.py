import datetime, random

with open("config.yaml", "r") as f:
    config = f.read()

niche = "fitness motivation"  # will later parse from config
today = datetime.date.today().strftime("%Y-%m-%d")

article = f"<h2>{today}: {niche.title()} Tip</h2><p>This is where your AI-generated content will go.</p>"

with open("index.html", "a") as f:
    f.write(article)

print("Article added to blog!")
