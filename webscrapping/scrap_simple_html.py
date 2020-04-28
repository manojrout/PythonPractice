from bs4 import BeautifulSoup
import requests

with open('simple.html') as html_file:
    soup = BeautifulSoup(html_file, 'lxml')

'''Prints html file in proper indentation'''
# print(soup.prettify())

'''Gets Title with header'''
# match = soup.title
'''Prints only text of the title'''
# match = soup.title.text

'''Gets first complete div tag'''
# match = soup.div

'''Gets the complete div where class is footer'''
# match = soup.find('div', class_='footer')

article = soup.find('div', class_='article')
print(article)
for article in soup.find_all('div', class_='article'):
    # print(article)

    '''Finds text of the anchor class of h2 inside article class'''
    headline = article.h2.a.text
    print(headline)

    summary = article.p.text
    print(summary)
    print()



