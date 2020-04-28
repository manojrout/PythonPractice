from bs4 import BeautifulSoup
import requests
import csv

url = 'https://www.moneycontrol.com/markets/indian-indices/top-nse-500-companies-list/7?classic=true'

source = requests.get(url).text
soup = BeautifulSoup(source, 'lxml')
csv_file = open('nifty_500_comp.csv', 'w')

table_body = soup.find('table', class_='responsive')
rows = table_body.find_all('tr')
# row_cells = []
csv_writer = csv.writer(csv_file)

for row in rows:
    if rows.index(row) == 0:
        th = row.getText().split('\n')
        csv_writer.writerow(th[1:-1])
    else:
        tr = row.getText().split('\n')
        csv_writer.writerow(tr[1:-1])

csv_file.close()

