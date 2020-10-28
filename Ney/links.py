import requests
import pandas as pd
from bs4 import BeautifulSoup

Links = []
page_number = 0 #pages for the url, separated for being more clear
n = 43 #this is number of pages in the website

with open("res.txt", "w") as output:
    for i in range(n):
        page_number +=1 
        URL = f"https://nashreney.com/products/page/{page_number}/"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        
        books = soup.find_all("a", class_="prgridwrap")
        for book in books:
#            LINK_tmp = book.find('a')
            LINK  = book.get('href')
            print(LINK)
#            print(page_number)
            output.write('{}\n'.format(LINK))

#df = pd.DataFrame(ALL, columns=['Links'])
#df.to_excel (r'/home/pilot/fun/Rekab/scrappers/output.xlsx', index = False, header=True, encoding='utf-8')
