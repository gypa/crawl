 #coding: utf-8
import requests
from lxml import etree
headers = {
'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/72.0.3626.109 Safari/537.36'
}
url = "https://www.37zw.net/14/14412/"
def get_bookname():
    response = requests.get(url).text.encode('iso-8859-1').decode('gbk')
    html = etree.HTML(response)
    bookname = html.xpath('//div[@id = "info"]/h1/text()')
    author = html.xpath('//div[@id = "info"]/p[1]/text()')
    content = "".join( author).replace("\xa0", "")
    # print(bookname, content)

get_bookname()

def get_html_content():
    response = requests.get(url).text.encode('iso-8859-1').decode('gbk')
    html = etree.HTML(response)
    content = html.xpath('//div[@id = "list"]/dl/dd/a/text()')
    link_html = html.xpath('//div[@id = "list"]/dl/dd/a/@href')
    temp = []
    for a in link_html:
        start_url = "https://www.37zw.net/14/14412/"
        all_url = start_url + a
        # print(all_url)
        temp.append(all_url)
    # print(temp)
    for i in temp:
        response = requests.get(i, headers=headers).text.encode('iso-8859-1').decode('gbk')
        html = etree.HTML(response)
        content = html.xpath('//div[@id = "content"]/text()')
        name = html.xpath('//div[@class= "bookname"]/h1/text()')
        chapter_content = "".join(content).replace('\xa0', "")
        chapter_name = "".join(name)
        print(chapter_name, chapter_content)
        with open("d:\\big.txt", "a")as f:
            f.write(chapter_name)
            f.write("\n\n")
            f.write(chapter_content)
            f.write("\n\n")



get_html_content()