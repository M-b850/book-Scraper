import requests
import pandas as pd
from bs4 import BeautifulSoup

names=[]
publishers = []
writers = []
ALL = {'Book':names, 'Publisher':publishers, 'Writer':writers}
page_number = 1
#for page_number in range(3):
URL = f"https://shahreketabonline.com/products/pn/{page_number}/"
page = requests.get(URL)
soup = BeautifulSoup(page.content, 'html.parser')

books = soup.find_all(
'div', class_='proItem'
)


#df = pd.DataFrame(ALL, columns=['Book', 'Publisher', 'Writer'])
#df.to_excel (r'/home/pilot/fun/Rekab/scrappers/output.xlsx', index = False, header=True, encoding='utf-8')