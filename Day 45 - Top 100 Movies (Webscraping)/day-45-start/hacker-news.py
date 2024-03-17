from bs4 import BeautifulSoup
import requests

response = requests.get(url="https://news.ycombinator.com/")
yc_web_page = response.text

soup = BeautifulSoup(yc_web_page, "html.parser")

articles = soup.select(selector=".titleline")
scores = soup.find_all(name="span", class_="score")

article_titles = []
article_links = []
article_scores = []

for article in articles:
    article_tag = article.select_one(selector="a")
    article_titles.append(article_tag.getText())
    article_links.append(article_tag.get("href"))

article_scores = [int(score.getText().split()[0]) for score in scores]

highest_score = max(article_scores)
highest_index = article_scores.index(highest_score)

highest_article_title = article_titles[highest_index]
highest_article_link = article_links[highest_index]

print(highest_article_title)
print(highest_article_link)
