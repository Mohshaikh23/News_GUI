import requests

class NewsApp:
    
    def __init__(self):
        
        data = requests.get('https://newsapi.org/v2/top-headlines?country=us&apiKey=42722ab23ecd4c73819259cefeb18972').json()
        
        print(data)

obj = NewsApp()

        
        