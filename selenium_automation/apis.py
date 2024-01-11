import requests

r = requests.get('https://newsapi.org/v2/everything?q=tesla&from=2023-11-07&sortBy=publishedAt&apiKey=7da0ea48863b4ff996b63a18a6fad984')
content = r.json()

articles = content['articles']

for article in articles:
    print("Titulo\n", article['title'], '\nDescripcion\n', article['description'],'\n\n')

def get_news(topic,from_date, to_date, language='en', api_key="7da0ea48863b4ff996b63a18a6fad984"):
    url = f'https://newsapi.org/v2/everything?q=tesla&from=2023-11-07&sortBy=publishedAt&apiKey=7da0ea48863b4ff996b63a18a6fad984'
