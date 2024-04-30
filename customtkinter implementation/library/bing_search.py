import requests
from configparser import ConfigParser
from bs4 import BeautifulSoup
from collections import defaultdict


class BingSearch:
    def __init__(self, api_key, endpoint):
        self.headers = {
            "Ocp-Apim-Subscription-Key": api_key
        }
        self.endpoint = endpoint
        
    def search(self, params):
        response = requests.request("GET", self.endpoint, headers=self.headers, params=params)
        return response
        
    def parse_url(self, response):
        search_value = response.json()['webPages']['value']
        urls = [value['url'] for value in search_value]
        return urls
    
    def parse_html(self, urls, search_range):
        website_text_content = defaultdict(lambda: "Error")
        
        for index in search_range:
            url = urls[index]
            content_response = requests.get(url)
            if content_response.status_code == 200:
                # Parse the HTML content
                soup = BeautifulSoup(content_response.content, 'html.parser')
                text_content = soup.get_text(separator='\n')
                website_text_content[url] = text_content
            else:
                website_text_content[url] = "Error"
        
        return website_text_content
        

def search(query):
    # Load the config info
    config = ConfigParser()
    config.read('config.ini')
    api_key = config['BingAPI']['api_key']

    # Set up the search engine endpoint
    endpoint = "https://api.bing.microsoft.com/v7.0/search"

    # Set up the search params
    # query = "how to \"FOIL\" two complex numbers"

    params = {
        'q': query,
        'count': 50, 
        'offset': 0,
        'mkt': 'en-US',
        'freshness': 'Month'
    }

    headers = {
        "Ocp-Apim-Subscription-Key": api_key
    }

    response = requests.request("GET", endpoint, headers=headers, params=params)
    search_value = response.json()['webPages']['value']
    urls = [value['url'] for value in search_value]
    website_text_content = {}
    url = urls[0]
    
    soup = BeautifulSoup(requests.get(url).content, 'html.parser')
    text_content = soup.get_text(separator='\n')
    website_text_content[url] = text_content
    
    # for url in urls:
    #     content_response = requests.get(url)
    #     if content_response.status_code == 200:
    #         # Parse the HTML content
    #         soup = BeautifulSoup(content_response.content, 'html.parser')
    #         text_content = soup.get_text(separator='\n')
    #         website_text_content[url] = text_content
    #     else:
    #         print(f"Error fetching content for {url}")
        
    return website_text_content


if __name__ == "__main__":
    # Load the config info
    config = ConfigParser()
    config.read('config.ini')
    api_key = config['BingAPI']['api_key']
    endpoint = config['BingAPI']['endpoint']
    
    model = BingSearch(api_key, endpoint)
    response = model.search({
        'q': "how to do matrix multiplication",
        'count': 50, 
        'offset': 0,
        'mkt': 'en-US',
        'freshness': 'Month'
    })
    urls = model.parse_url(response)
    html = model.parse_html(urls, range(1))
    print(html)

