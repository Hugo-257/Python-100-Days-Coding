from bs4 import BeautifulSoup
import requests
import codecs

response=requests.get("https://www.timeout.com/newyork/movies/best-movies-of-all-time")
content=response.text

soup=BeautifulSoup(content,'lxml')
movies=soup.find_all(name="h3",class_="_h3_cuogz_1")
movies.reverse()
for movie in movies:
   
    with codecs.open("Top 100 Movies.txt","a", "utf-8") as f:
        movieDetails=movie.getText()
        f.write(f'{movieDetails} \n')

