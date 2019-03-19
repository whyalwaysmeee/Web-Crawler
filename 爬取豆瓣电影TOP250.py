from pyquery import PyQuery as pq             #pyquery解析库
from bs4 import BeautifulSoup                 #beautifulsoup解析库
import time                                   #时间函数
from selenium import webdriver                #selenium库中的webdriver用于模拟浏览器
import re                                     #用于处理正则表达式，因为有一部分的数据需要提取中文
import codecs

"""使用pyquery爬取该页上的电影的名称，并用列表储存
不知因为什么原因爬取下来的文本中出现了一些乱码，所以采用编码和解码的函数仅将中文提取出来，让结果更便于查看"""
def getnames(doc):
    try:
        list_name = []
        list_name_chinese = []
        movienames = doc('.info .title').items()
        for movie_name in movienames:
            list_name.append(movie_name.text())
        for item in list_name:
            s = item.encode('utf-8')
            s = s.decode('utf8')
            m = re.findall(u"[\u4e00-\u9fa5]+", s)
            list_name_chinese.extend(m)
        return list_name_chinese
    except TimeoutError:
        return getnames(doc)

"""使用pyquery爬取该页上的电影的别名，并用列表储存"""
def getothernames(soup):
    try:
        list_othername = []
        movieothernames = doc('.hd .other').items()
        for movie_othername in movieothernames:
            list_othername.append(movie_othername.text())
        return list_othername
    except TimeoutError:
        return getothernames(soup)

"""使用beautifulsoup爬取该页上的电影的人员，并用列表储存
这里不使用pyquery的原因是它无法找到对应的标签（其实是本人水平受限）
这个函数的运行结果有点瑕疵，出现了大量空格和xa0这样的乱码"""
def getstars(doc):
    try:
        list_stars = []
        moviestars = soup.find_all('p', attrs={'class': ''})
        for movie_stars in moviestars:
            list_stars.append(movie_stars.get_text())
        return list_stars
    except TimeoutError:
        return  getstars(doc)

"""使用pyquery爬取该页上的电影的评分，并用列表储存"""
def getscores(doc):
    try:
        list_scores = []
        moviescores = doc('.grid_view .star .rating_num').items()
        for movie_scores in moviescores:
            list_scores.append(movie_scores.text())
        return list_scores
    except TimeoutError:
        return getscores(doc)

"""使用pyquery爬取该页上的电影的一句话简介，并用列表储存"""
def getquotes(doc):
    try:
        list_quotes = []
        moviequotes = doc('.grid_view .quote').items()
        for movie_quotes in moviequotes:
            list_quotes.append(movie_quotes.text())
        return list_quotes
    except TimeoutError:
        return getquotes(doc)

"""主函数，测试功能
我们的爬取目标是豆瓣电影top250网站上的所有电影的基本信息，我将其分为五个信息类别，分别是名称、别名、人员、评分和一句话简介
想按单个电影的信息来分也很容易，把每个列表按下标依次提取元素就行了
爬取结果中有一些莫名的字符，恕本人非科班出身，才疏学浅，水平有限，无法解决"""
if __name__ == "__main__":
    """打开或新建一个文本文档，用于储存爬取的电影信息，此处要用codecs进行编码，否则将无法写入汉字"""
    fw = codecs.open("D:/cs/P3/电影.txt",'w+','utf-8')

    """获取浏览器信息，防止反爬，一般不需要，加上也无妨"""
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/68.0.3440.106 Safari/537.36'}

    url = "https://movie.douban.com/top250"         #获取要爬取网页的地址，复制粘贴即可
    browser = webdriver.Chrome()                    #利用webdriver模拟打开Chrome浏览器
    browser.get(url)                                #模拟在浏览器地址栏中输入网站地址

    """创建新列表，用于储存爬取的结果"""
    names = []
    othernames = []
    stars = []
    scores = []
    quotes = []

    """这里采用一个循环，因为要爬取所有10页里的250个电影的信息
    10这个页数是我人为输入的，也可以编写程序获得，我能想到的方法就是先获取250这个数字，这很容易，然后先爬一页，随便选获得的5个列表中的1个的长度就是每一页的电影量，然后再相除一下即得到页数"""
    for i in range(10):
        html = browser.page_source                 #这个函数很重要，获取当前页面的源代码，没它无法实现翻页
        doc = pq(html)                             #将网页源代码变为可用pyquery进行解析的形式
        soup = BeautifulSoup(html, 'lxml')         #将网页源代码变为可用beautifulsoup进行解析的形式

        """每一次循环，也就是每翻一页，都将新一页中爬取的以列表为形式的结果，用extend函数添加到大的列表中去"""
        names.extend(getnames(doc))
        othernames.extend(getothernames(doc))
        stars.extend(getstars(soup))
        scores.extend(getscores(doc))
        quotes.extend(getquotes(doc))

        button = browser.find_element_by_class_name('next')         #翻页操作的精髓所在，找到网页中的“下一页”按钮
        button.click()                                              #点击实现翻页
        time.sleep(1)                                               #睡一秒让机器缓缓，Pycharm还是很占内存的，每次一跑起来呼呼地叫

    """打印结果"""
    print(names)
    print(othernames)
    print(stars)
    print(scores)
    print(quotes)

    """把每个列表的信息依次写入文本文档"""
    for a in names:
        fw.write(a)
        fw.write(" ")
    fw.write("\n")
    for a in othernames:
        fw.write(a)
        fw.write(" ")
    fw.write("\n")
    for a in stars:
        fw.write(a)
        fw.write(" ")
    fw.write("\n")
    for a in scores:
        fw.write(a)
        fw.write(" ")
    fw.write("\n")
    for a in quotes:
        fw.write(a)
        fw.write(" ")

    time.sleep(3)
    browser.close()                               #爬取完毕，关闭浏览器