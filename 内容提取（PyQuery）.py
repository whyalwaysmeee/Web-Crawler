from pyquery import PyQuery as pq
import requests

def getnames(doc):
    list_name = []
    booknames = doc('.more-meta .title').items()
    for book_name in booknames:
        list_name.append(book_name.text())
    return(list_name)

def getauthors(doc):
    list_author = []
    bookauthors = doc('.more-meta .author').items()
    for book_author in bookauthors:
        list_author.append(book_author.text())
    return(list_author)


def getyears(doc):
    list_year = []
    bookyears = doc('.year').items()
    for book_year in bookyears:
        list_year.append(book_year.text())
    return(list_year)

def getpublishers(doc):
    list_publisher = []
    bookpublishers = doc('.publisher').items()
    for book_publisher in bookpublishers:
        list_publisher.append(book_publisher.text())
    return(list_publisher)

def getabstracts(doc):
    list_abstract = []
    bookabstract = doc('.abstract').items()
    for book_abstract in bookabstract:
        list_abstract.append(book_abstract.text())
    return(list_abstract)

if __name__ == "__main__":
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}
    html = requests.get("https://book.douban.com/", headers=headers).text
    doc = pq(html)
    print("书籍名称：")
    for item in getnames(doc):
        print(item)
    print('\n')
    print("书籍作者：")
    for item in getauthors(doc):
        print(item)
    print('\n')
    print("书籍年份：")
    for item in getyears(doc):
        print(item)
    print('\n')
    print("书籍出版社：")
    for item in getpublishers(doc):
        print(item)
    print('\n')
    print("书籍简介：")
    for item in getabstracts(doc):
        print(item)