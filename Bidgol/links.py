import requests
import pandas as pd
from bs4 import BeautifulSoup

Links = []
names=[]
publishers = []
ALL = {'Book':names, 'Publisher':publishers,'Links': Links}
page_number = 0

for i in range(17):
    page_number +=1
    URL = f"http://www.bidgolpublishing.com/Books.aspx?t=0&p={page_number}&l=&c=0"
    page = requests.get(URL)
    soup = BeautifulSoup(page.content, 'html.parser')
    books = soup.find_all(
    '', target='_blank'
    )
    for book in books:
        LINK  = book.get('href')
        if 'Id' in LINK:
            Links.append(f"http://www.bidgolpublishing.com/{LINK}")
           
    '''
    for book in books:
        name = book.find('p', class_='card-text font-12 box-name-h').text.strip()
        publisher = book.find('p', class_='card-text font-12').text.strip()
        link  = 'https://www.30book.com'
        link += book.find('a', target="_blank").get('href')
        names.append(name)
        publishers.append(publisher)
'''
#df = pd.DataFrame(ALL, columns=['Links'])
#df.to_excel (r'/home/pilot/fun/Rekab/scrappers/output.xlsx', index = False, header=True, encoding='utf-8')
