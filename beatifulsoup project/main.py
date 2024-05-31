from bs4 import BeautifulSoup
import requests

# with open("website.html",encoding='utf-8') as file:
#     contents=file.read()


# soup=BeautifulSoup(contents,'html.parser')

# print(soup.find_all(name='a'))

# print(soup.select_one(selector='p a'))

# response=requests.get('https://news.ycombinator.com/news')
# yc_web_page=response.text

# soup=BeautifulSoup(yc_web_page,'html.parser')
# print(soup.select('.title .titleline a'))

# print(soup.select_one('.score').get_text())

response=requests.get("https://web.archive.org/web/20200518073855/https://www.empireonline.com/movies/features/best-movies-2/")
top_100_movies=response.text

soup=BeautifulSoup(top_100_movies,'html.parser')
movies=soup.find_all('h3',attrs={'class':'title'})
movies=movies[::-1]
for movie in movies:
    with open('movies.txt','a',encoding='utf-8') as file:
        file.write(movie.get_text()+'\n')