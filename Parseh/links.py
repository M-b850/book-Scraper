import requests
import pandas as pd
from bs4 import BeautifulSoup

Links = []
page_number = 0 #pages for the url, separated for being more clear
n = 10 #this is number of pages in the website

with open("res2.txt", "w") as output:
    for i in range(n):
        page_number +=1 
        URL = f"http://www.parsehbook.com/category/%da%a9%d9%88%d8%af%da%a9-%d9%88-%d9%86%d9%88%d8%ac%d9%88%d8%a7%d9%86/%d9%85%d8%ac%d9%85%d9%88%d8%b9%db%80-%d9%86%db%8c%da%a9%d9%88%d9%84%d8%a7-%da%a9%d9%88%da%86%d9%88%d9%84%d9%88/?pg={page_number}"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        books = soup.find_all("li", class_="fRight")
        for book in books:
            LINK_tmp = book.find('a', href=True)
            LINK = LINK_tmp['href']
            print(LINK)
#            print(page_number)
            output.write('{}\n'.format(LINK))

#df = pd.DataFrame(ALL, columns=['Links'])
#df.to_excel (r'/home/pilot/fun/Rekab/scrappers/output.xlsx', index = False, header=True, encoding='utf-8')