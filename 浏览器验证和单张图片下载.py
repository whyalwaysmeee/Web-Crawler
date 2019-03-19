import requests
headers= {'User-Agent':'Mozilla/5.0 (Windows NT 6.3; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.90 Safari/537.36 2345Explorer/9.3.2.17331'}
response= requests.get("https://www.zhihu.com/",headers= headers)


url = requests.get("https://static.zhihu.com/heifetz/logo.f6eef03354bbf46f4e04.png")
type(url.content)
with open('1.png','wb') as f:
    f.write(response.content)
    f.close