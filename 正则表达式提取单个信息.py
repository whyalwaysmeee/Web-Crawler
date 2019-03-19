import re
import requests
url = requests.get('https://book.douban.com/').text
pattern = re.compile('<li.*?cover.*?href="(.*?)".*?title="(.*?)".*?more-meta.*?author(.*?)</span>.*?year(.*?)</span>.*?</li>', re.S)
results = re.search(pattern, url)
print(results.groups())