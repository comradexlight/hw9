import requests
from bs4 import BeautifulSoup


url = 'https://stackoverflow.com/questions/'

params = {
    'tag': 'python',
    'creation': '2daysAgo',
    'order': 'asc',
    'sort': 'creation'
}

res = requests.get(url=url, params=params)

soup = BeautifulSoup(res.text, "html.parser")

questions = soup.select(".question-summary")

for que in questions:
    q = que.select_one('.question-hyperlink').getText()
    print(q)