from bs4 import BeautifulSoup
import requests
# URL of the Wikipedia page
url = 'https://en.wikipedia.org/wiki/List_of_countries_by_number_of_Internet_users'
page = requests.get(url)
soup = BeautifulSoup(page.text, 'html')
print(soup)
table = soup.find_all('table')[5]
print(table)
internet = table.find_all('th')
internet
internet = [title.text.strip() for title in internet]
print(internet)
ins = []
internet[5] = 'Population(2021)'
print(internet)
import pandas as pd
df = pd.DataFrame(columns = internet)
df
column_data = table.find_all('tr')
for row in table.find_all('tr')[1:]:  # Skipping the header row
    row_data = row.find_all('td')
    individual_row_data = [data.text.strip() for data in row_data]
    
    # Only append rows that match the number of columns
    if len(individual_row_data) == len(internet):
        length = len(df)
        df.loc[length] = individual_row_data
df
df.to_csv(r'C:\Users\Dell\Desktop\DREAM\DataSets\Internet.csv', index = False)
