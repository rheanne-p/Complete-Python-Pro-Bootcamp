import requests
from bs4 import BeautifulSoup

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

empire_html = requests.get(url=URL).text

soup = BeautifulSoup(empire_html, "html.parser")
titles = soup.select(selector=".article-title-description__text .title")

titles_list = [title.getText() for title in titles]

with open(file="top-100.txt", mode="w", encoding="utf-8") as txt_file:
    for num in range(99, -1, -1):
        txt_file.write(f"{titles_list[num]} \n")
