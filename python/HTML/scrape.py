# -*- coding -*-
import requests
from bs4 import BeautifulSoup
from requests.compat import urljoin

#url = "http://tistory.com/category/travel"
url = "https://www.clien.net/service/board/cm_car"

res = requests.get(url)
soup = BeautifulSoup(res.content, "html.parser")

lists = soup.find_all("div", {"class":"list_item symph_row"})

for content in lists:
    divs = content.find_all('div')
    like_count = divs[0].get_text()

    link = divs[1].a
    spans = link.find_all('span')

    category = spans[0].get_text()
    title = spans[1].get_text()

    h_link = urljoin(url, link.get('href'))
    
    author = divs[2].get_text().strip()
    if author == "":
        author = divs[2].img.get('alt')

    print u"{0} | {1}({2})\n {3}\n - {4} -\n".format(category, title, like_count, h_link, author) # repr(author)
    