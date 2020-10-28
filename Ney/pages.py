import requests
import pandas as pd
from bs4 import BeautifulSoup
import io

book=[]
author=[]
author_fa=[]
translator=[]
pages=[]
shabak=[]
publish=[]
qte=[]
jeld=[]
vazn = []

ALL = {
    'Book':book,
    'Author-Farsi':author_fa, 'Author-English':author,
    'Translator':translator,'Pages':pages,
    'Shabak':shabak,'Publish':publish,
    'QTE':qte, 'Jeld':jeld, "Vazn":vazn,
    }
with io.open("res.txt", "r", newline=None) as fd:
    for line in fd:
        URL = line.replace("\n", "")
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        BOOK = soup.find('h1', class_='product_title entry-title').text.strip()
        temp_names  = soup.find_all('div', class_="bookauthorssingle")
        temp_numbs = soup.find_all('span', class_="wrapcontnettable")
        try:
            AUTHOR_FA = temp_names[0].text.strip()
        except IndexError:
            AUTHOR_FA = ''
        try:
            TRANSLATOR = temp_names[1].text.strip()
            SHABAK = temp_numbs[3].text.strip()
            PAGES = temp_numbs[5].text.strip()
            PUBLISH = temp_numbs[7].text.strip()
            QTE = temp_numbs[9].text.strip()
            JELD = temp_numbs[11].text.strip()
            try :
                VAZN = temp_numbs[13].text.strip()
            except IndexError:
                VAZN = ''
        except IndexError:
            TRANSLATOR = ''
            SHABAK = temp_numbs[2].text.strip()
            PAGES = temp_numbs[4].text.strip()
            PUBLISH = temp_numbs[5].text.strip()
            QTE = temp_numbs[8].text.strip()
            JELD = temp_numbs[10].text.strip()
            try :
                VAZN = temp_numbs[12].text.strip()
            except IndexError:
                VAZN = ''
        book.append(BOOK)
        author_fa.append(AUTHOR_FA)
        translator.append(TRANSLATOR)
        shabak.append(SHABAK)
        pages.append(PAGES)
        publish.append(PUBLISH)
        qte.append(QTE)
        jeld.append(JELD)
        vazn.append(VAZN)

df = pd.DataFrame(
    ALL, columns=
    [
        'Book',
        #'BookSub',
        #'Author-English',
        'Author-Farsi',
        'Translator',
        'Shabak',
        'Publish',
        'QTE',
        'Jeld',
        'Pages',
        'Vazn',
    ]
)
df.to_excel (r'/home/pilot/fun/book-Scraper/Ney/output.xlsx', index = False, header=True, encoding='utf-8')
