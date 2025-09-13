import requests
from bs4 import BeautifulSoup
import pandas as pd

URL = 'https://news.ycombinator.com/'  # Example website

response = requests.get(URL)
if response.status_code != 200:
    print(f"Failed to fetch page, status code: {response.status_code}")
    exit()

soup = BeautifulSoup(response.text, 'html.parser')

# Extract news titles
items = soup.select('.storylink')
titles = [item.get_text() for item in items]

# Save to CSV
df = pd.DataFrame(titles, columns=['Title'])
df.to_csv('news_titles.csv', index=False)

print(f"Saved {len(titles)} titles to news_titles.csv")