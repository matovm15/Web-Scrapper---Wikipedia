from bs4 import BeautifulSoup
import requests
import pandas as pd
import matplotlib.pyplot as plt
import numpy as np

webpage = requests.get(
    'https://s3.amazonaws.com/codecademy-content/courses/beautifulsoup/cacao/index.html')
soup = BeautifulSoup(webpage.content, 'html.parser')
#print(soup)

webpg_ratings = soup.find_all(attrs={"class": "Rating"})
ratings = []
for rating in webpg_ratings[1:]:
  ratings.append(float(rating.string))
#print(ratings)
plt.hist(ratings)
plt.show()
com_name = soup.select(".Company")
company_name = []
for name in com_name[1:]:
  company_name.append(name.string)
#print(company_name)
dict = {"company_name": company_name, "ratings": ratings}
df = pd.DataFrame.from_dict(dict)
mean_values = df.groupby('company_name').ratings.mean()
best_10 = mean_values.nlargest(10)
print(best_10)
