from bs4 import BeautifulSoup
import requests
import xlrd
import xlwt

headers = {'User-Agent':'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
#浏览器验证，防反爬

html = requests.get("https://movie.douban.com/top250",headers=headers).text
#获取网页源代码

soup = BeautifulSoup(html, 'lxml')
#解析网页



movie_name = soup.find_all('span', attrs={'class': 'title'})
print('电影名称及外文名：')
for item in movie_name:
    print(item.get_text())

movie_othername = soup.find_all('span', attrs={'class': 'other'})
print('电影别名：')
for item in movie_othername:
    print(item.get_text())

movie_stuff = soup.find_all('p', attrs={'class': ''})
print('电影人员及电影类型：')
for item in movie_stuff:
    print(item.get_text())

movie_score = soup.find_all('span', attrs={'class': 'rating_num'})
print('电影评分：')
for item in movie_score:
    print(item.get_text())

movie_briefintroduction = soup.find_all('span', attrs={'class': 'inq'})
print('电影一句话简介：')
for item in movie_briefintroduction:
    print(item.get_text())

