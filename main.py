from bs4 import BeautifulSoup
import requests

URL = "https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/"
response = requests.get(URL)
website_html = response.text

soup = BeautifulSoup(website_html, "html.parser")

top_movies = soup.find_all(name="h3", class_="title")
movie_title = [movie.getText() for movie in top_movies]
movies = movie_title[::-1]
print(movies)

with open("movies.txt", mode="w") as file:
    for movie in movies:
        print(movie)
        file.write(f"{movie}\n")
