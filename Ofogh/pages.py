import requests
import pandas as pd
from bs4 import BeautifulSoup
import io

book=[]
author_fa=[]

ALL = {
    'Book':book, 'Author-Farsi':author_fa
    }
with io.open("res.txt", "r", newline=None) as fd:
    for line in fd:
        URL = line.replace("\n", "")
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        BOOK = soup.find('h2', class_='product_title entry-title').text.strip()
        AUTHOR_FA2 = soup.find('span', class_='yith-wcbr-brands')
        AUTHOR_FA = AUTHOR_FA2.find('a').text.strip()
        author_fa.append(AUTHOR_FA)
        book.append(BOOK)


df = pd.DataFrame(
    ALL, columns=
    [
        'Book',
        #'BookSub',
        #'Author-English',
        'Author-Farsi',
        #'Translator',
        #'Shabak',
        #'Publish',
        #'QTE',
        #'Jeld',
        #'Pages',
    ]
)
df.to_excel (r'/home/pilot/fun/book-Scraper/Ofogh/output.xlsx', index = False, header=True, encoding='utf-8')
