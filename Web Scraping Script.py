import requests
from bs4 import BeautifulSoup

def scrape_product_data(url):
    headers = {"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"}
    response = requests.get(url, headers=headers)
    soup = BeautifulSoup(response.content, 'html.parser')
    
    title = soup.find('span', {'id': 'productTitle'}).text.strip()
    
    price = soup.find('span', {'id': 'priceblock_ourprice'}).text.strip()
    
    rating = soup.find('span', {'class': 'a-icon-alt'}).text.strip()
    
    return {'Title': title, 'Price': price, 'Rating': rating}

# Usage example
product_data = scrape_product_data('https://www.amazon.com/dp/B08F7C7JFT')
print(product_data)
