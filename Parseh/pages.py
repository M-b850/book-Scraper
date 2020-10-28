import requests
import pandas as pd
from bs4 import BeautifulSoup
import io

book=[]
author_fa=[]
translator=[]
pages=[]
shabak=[]
publish=[]
qte=[]
jeld=[]
vir = []

ALL = {
    'Book':book,
    'Author-Farsi':author_fa,
    'Translator':translator,
    'Pages':pages,
    'Shabak':shabak,
    'Publish':publish,
    'Qte':qte,
    'Jeld':jeld,
    'Vir':vir, 
}
with io.open("res.txt", "r", newline=None) as fd:
    for line in fd:
        URL = line.replace("\n", "")
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        INFO_t = soup.find('div', id='bookInfo')
        INFO = INFO_t.find('ul')
        BOOK = soup.find('h3').text.strip()
        detail = INFO.find_all('li')
        AUTHOR_FA = ''
        PAGES = ''
        VIR = ''
        PUBLISH = ''
        QTE = ''
        JELD = ''
        SHABAK = ''
        TRANSLATOR = ''
        for i in range(len(detail)):
            if "نویسنده" in detail[i].text.strip():
                AUTHOR_FA = detail[i].find('a').text.strip()
            elif 'تعداد صفحات' in detail[i].text.strip():
                PAGES = detail[i].find('span').text.strip()
            elif 'مصحح' in detail[i].text.strip():
                VIR = detail[i].find('a').text.strip()
            elif 'سال انتشار' in detail[i].text.strip():
                PUBLISH = detail[i].find('span').text.strip()
            elif 'قطع' in detail[i].text.strip():
                QTE = detail[i].find('span').text.strip()
            elif 'نوع جلد' in detail[i].text.strip():
                JELD = detail[i].find('span').text.strip()
            elif 'شابک' in detail[i].text.strip():
                SHABAK = detail[i].find('span').text.strip()
            elif 'مترجم' in detail[i].text.strip():
                TRANSLATOR = detail[i].find('a').text.strip()

        author_fa.append(AUTHOR_FA)
        book.append(BOOK)
        vir.append(VIR)
        publish.append(PUBLISH)
        translator.append(TRANSLATOR)
        pages.append(PAGES)
        qte.append(QTE)
        jeld.append(JELD)
        shabak.append(SHABAK)

df = pd.DataFrame(
    ALL, columns=
    [
    'Book',
    'Author-Farsi',
    'Translator',
    'Pages',
    'Shabak',
    'Publish',
    'Qte',
    'Jeld',
    'Vir', 
    ]
)
df.to_excel (r'/home/pilot/fun/book-Scraper/Parseh/output.xlsx', index = False, header=True, encoding='utf-8')