from bs4 import BeautifulSoup
import requests
import re

url = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"

webpage_contents = requests.get(url).text
soup = BeautifulSoup(webpage_contents, "html.parser")
movies_titles = soup.select("h3.title")


movies_by_rank = [(int(re.split(r"\)|\:", title.getText())[0].strip())
                   , re.split(r"\)|\:", title.getText())[1].strip()) for title in movies_titles]

sorted_movies = sorted(movies_by_rank, key=lambda x: x[0])

# save to a file

with open("top_100_movies.txt", "w") as movies_list_file:
    for movie in sorted_movies:
        movies_list_file.write(f"{ movie[0]}) {movie[1]}\n")
    print("success..")


