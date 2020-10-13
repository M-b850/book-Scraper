import requests
import pandas as pd
from bs4 import BeautifulSoup

Links = []
names=[]
publishers = []
ALL = {'Book':names, 'Publisher':publishers,'Links': Links}
page_number = 0
with open("res.txt", "w") as output:
    for i in range(93):
        page_number +=1
        URL = f"http://salesspublication.com/index.php?route=product/search&search=&page={page_number}"
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        books = soup.find_all(
        'div', class_='image'
        )
        for book in books:
            Link2 = book.find('a')
            LINK  = Link2.get('href')
            print(LINK)
            output.write('{}\n'.format(LINK))
    
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
