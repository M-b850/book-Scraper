import requests
import pandas as pd
from bs4 import BeautifulSoup, NavigableString, Tag
import io
import re

book=[]
author=[]
author_fa=[]
translator=[]
pages=[]
shabak=[]
publish=[]
qte=[]
jeld=[]
booksub=[]

ALL = {
    'Book':book, 'Publisher':"بیدگل", 'BookSub':booksub,
    'Author-Farsi':author_fa, 'Author-English':author,
    'Translator':translator,'Pages':pages,
    'Shabak':shabak,'Publish':publish,
    'QTE':qte, 'Jeld':jeld,

    }
with io.open("res.txt", "r", newline=None) as fd:
    for line in fd:
        URL = line.replace("\n", "")
        print(URL)
        page = requests.get(URL)
        soup = BeautifulSoup(page.content, 'html.parser')
        info = soup.find('div', class_='col-md-3 col-sm-6 book-txt-col')
        
        ###info
        BOOK = info.find('h1', 'head1').text.strip()
        booksub_tmp = info.find('h2', 'head2').text.strip()

        AUTHOR = info.find('h2', 'head2 maintitle').text.strip()
        h3 = info.find_all('h3', 'head3')
        AUTHOR_FA = h3[0].text.strip()
        try:
            TRANSLATOR = h3[1].text.strip()
        except IndexError:
            TRANSLATOR = ''
        book.append(BOOK)
        booksub.append(booksub_tmp)
        author.append(AUTHOR)
        author_fa.append(AUTHOR_FA)
        translator.append(TRANSLATOR)

        ###br tags
        tmp =[]
        tmp2 = []
        for br in info.findAll('br'):
            next_s = br.nextSibling
            if not (next_s and isinstance(next_s,NavigableString)):
                continue
            next2_s = next_s.nextSibling
            if next2_s and isinstance(next2_s,Tag) and next2_s.name == 'br':
                text = str(next_s).strip()
                if text:
                    tmp.append(next_s.lstrip().rstrip())
        for string in info.stripped_strings:
            tmp2.append(repr(string))
        subs = 'تعداد صفحات:'
        res = [i for i in tmp2 if subs in i] 
        pages.append(re.search(r'\d+', res[0]).group())
       

        shabak_tmp = tmp[0][7:]
        shabak_tmp = shabak_tmp.split('-')
        shabak_tmp = '-'.join(shabak_tmp[::-1])
        shabak.append(shabak_tmp)
        qte.append(tmp[3][6:])
        jeld.append(tmp[4][6:])

        

df = pd.DataFrame(
    ALL, columns=
    [
        'Book',
        'BookSub',
        'Author-English',
        'Author-Farsi',
        'Translator',
        'Shabak',
        #'Publish',
        'QTE',
        'Jeld',
        'Pages',
    ]
)
df.to_excel (r'/home/pilot/fun/Rekab/scrappers/output.xlsx', index = False, header=True, encoding='utf-8')