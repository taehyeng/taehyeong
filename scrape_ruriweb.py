# -*- coding -*-
import requests
from bs4 import BeautifulSoup as Soup
from requests.compat import urljoin

#url = 'http://bbs.ruliweb.com/news/board/1020/list?&cate=2'
url = 'http://bbs.ruliweb.com/news/board/1020'
res = requests.get(url)
soup = Soup(res.content, "html.parser")

rows = soup.find_all('tr', class_="table_body")
for row in rows:
    r_classes = row.get('class')

    if u'notice' in r_classes:
        continue
    else:
        id_num = row.find(class_='id').get_text().strip()
        category = row.find(class_='divsn').get_text().strip()
        title = row.find(class_='deco').get_text().strip()
        writer = row.find(class_='writer text_over').get_text().strip()
        recom = row.find(class_='recomd').get_text().strip()
        hit = row.find(class_='hit').get_text().strip()
        time = row.find(class_='time').get_text().strip()

        if recom > 5:
            print u"{0}-{1}-{2}:({3})-{4}-{5}\n".format(id_num, category, title, recom, writer, hit)

            link = row.find(class_="relative").find("a")

            url2 = link.get("href")
            res2 = requests.get(url2)
            soup2 = Soup(res2.content, "html.parser")
            print "===========BEST============="
        
            tmprows2 = soup2.find('div', class_="comment_view best row")
            rows2 = tmprows2.find_all('tr')
            # print rows2
        
            for row2 in rows2:
                try:
                    best_id = row2.find(class_='nick').get_text()
                    best_comment = row2.find(class_='text').get_text()
                    print u"{0}-{1}".format(best_id, best_comment)
                    print "-----------------------------"
                except:
                    pass
        
