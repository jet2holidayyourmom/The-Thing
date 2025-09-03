import yaml
import datetime
import os
import requests

# --- Step 1: Load config ---
with open("config.yaml", "r") as f:
    config = yaml.safe_load(f)

niche = config['content']['niche']
style = config['content']['style']
image_prompt = config['content']['image_prompt']
affiliate_link = config.get('affiliate_link', '')
donate_link = config.get('donate_link', '')

today = datetime.date.today().strftime("%Y-%m-%d")

# --- Step 2: Generate Article (placeholder AI) ---
# Replace this with a real AI API call if you have one
text = f"Today's conspiracy theory ({today}): Secrets unfold about {niche}..."

# --- Step 3: Generate Image ---
# For now we use Unsplash random image based on niche
img_url = f"https://source.unsplash.com/800x400/?{niche.replace(' ','-')}"

# --- Step 4: Build post HTML ---
article_html = f"""
<h2>{today}: {niche.title()} Theory</h2>
<img src="{img_url}" style="width:100%"/>
<p>{text}</p>
<p>Affiliate: <a href="{affiliate_link}" target="_blank">{affiliate_link}</a></p>
<p>Donate: <a href="{donate_link}" target="_blank">{donate_link}</a></p>
<hr/>
"""

# --- Step 5: Prepend to blog ---
if not os.path.exists("index.html"):
    with open("index.html", "w") as f:
        f.write("<h1>Conspiracy Blog</h1>\n")

with open("index.html", "r") as f:
    old = f.read()

with open("index.html", "w") as f:
    f.write(article_html + old)

print("✅ New conspiracy post added to blog")
