from bs4 import BeautifulSoup
import requests
# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_most-followed_Instagram_accounts'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
insta = table.find_all('th')
insta
insta = [title.text.strip() for title in insta]
print(insta)
ins = []
for i in range(len(insta)-1):
    ins.append(insta[i])
print(ins)
import pandas as pd
df = pd.DataFrame(columns = ins)
df
column_data = table.find_all('tr')
for row in table.find_all('tr')[1:]:  # Skipping the header row
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    # Only append rows that match the number of columns
    if len(individual_row_data) == len(ins):
        length = len(df)
        df.loc[length] = individual_row_data
df
df.to_csv(r'C:\Users\Dell\Desktop\DREAM\DataSets\Instagram.csv', index = False)
