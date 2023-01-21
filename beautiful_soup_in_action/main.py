from bs4 import BeautifulSoup
import requests
import math

url = "https://news.ycombinator.com/news"

ycomb_webpage = requests.get(url).text

soup = BeautifulSoup(ycomb_webpage, "html.parser")

anchors = soup.select("span.titleline > a")
vote_scores = soup.select("span.score")

anchor_texts = []
anchor_urls = []

for anchor in anchors:
    anchor_texts.append(anchor.getText())
    anchor_urls.append(anchor.get("href"))

scores = [int(score.getText().split()[0]) for score in vote_scores]

# print(anchor_texts)
# print(anchor_urls)
# print(scores)

print(anchor_texts[scores.index(max(scores))])
print(anchor_urls[scores.index(max(scores))])