from bs4 import BeautifulSoup
import requests
import pandas as pd

'''
1. We shall be scrapping a table of Highest Mountains Peaks in Africa on wikipedia
2. The table is made-up of 98 rows and 9 Columns
3. We're going to create a new table from the original copy and it'll contain only a few columns relevant to this Project
4. The New Table will include only 3 columns
5. The new table will be saved in a csv file which will then be retrived using tkinter
6. A New Python file (output.py) is used to display the saved csv in table format
'''

url = 'https://en.wikipedia.org/wiki/List_of_highest_mountain_peaks_of_Africa'
webpage = requests.get(url)
soup = BeautifulSoup(webpage.content, 'html.parser')
# print(soup)  # print the beautiful object
moutains = soup.find('table', {"class": "wikitable sortable"})
# print(moutains) # pribts the selected table
dfs = pd.read_html(str(moutains))
df = dfs[0]
# print(df.columns)

new_table =  df[['Country','Mountain[2]','Height (m)[3]']]
# saving the table to a csv file
new_table.to_csv('Mountain Peaks.csv')
#print(new_table)
