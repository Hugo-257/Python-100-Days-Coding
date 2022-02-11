from bs4 import BeautifulSoup
import requests
""" with open('website.html',encoding="utf8") as file:
    contents=file.read()
    
soup=BeautifulSoup(contents,'lxml')

print(soup("p").string) """

#Scrapping live website

response=requests.get("https://news.ycombinator.com/news")

contents=response.text
soup=BeautifulSoup(contents,'lxml')
titles=soup.find_all("a", {"class": "titlelink"})

for title in titles:
    print(title.getText())
    print(title.get("href"))
    

