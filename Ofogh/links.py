import requests
import pandas as pd
from bs4 import BeautifulSoup

Links = []
page_number = 0 #pages for the url, separated for being more clear
n = 63 #this is number of pages in the website

with open("res2.txt", "w") as output:
    for i in range(10):
        page_number +=1 
        URL = f"https://ofoqbooks.com/shop/page/{page_number}/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        books = soup.find_all("div", class_="product-content")
        for book in books:
            LINK_tmp = book.find('a')
            LINK  = LINK_tmp.get('href')
            print(page_number)
            output.write('{}\n'.format(LINK))


#df = pd.DataFrame(ALL, columns=['Links'])
#df.to_excel (r'/home/pilot/fun/Rekab/scrappers/output.xlsx', index = False, header=True, encoding='utf-8')
