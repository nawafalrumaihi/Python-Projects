import requests
from bs4 import BeautifulSoup
import time

# Specify the NewEgg product URL to monitor
url = 'https://www.newegg.com/global/bh-en/asus-geforce-rtx-4090-rog-strix-rtx4090-o24g-gaming/p/N82E16814126593?Description=GeForce%20RTX%204090&cm_re=GeForce_RTX%204090-_-14-126-593-_-Product&quicklink=true'

# Initialize empty variables for the previous and current product data
previous_data = ''
current_data = ''

# Run the web scraping loop indefinitely
while True:
    # Send a GET request to the NewEgg product page
    response = requests.get(url)

    # Parse the HTML content using BeautifulSoup
    soup = BeautifulSoup(response.content, 'html.parser')

    # Extract the product title and price from the page
    product_title = soup.find('h1', class_='product-title').text.strip()
    product_price = soup.select_one('div.price-current strong').text.strip()

    # Combine the product title and price into a single string
    current_data = f'{product_title} ({product_price})'

    # Check if the product data has changed since the previous scrape
    if current_data != previous_data:
        print('Product data has changed!')
        print(f'Previous data: {previous_data}')
        print(f'Current data: {current_data}')

        # Update the previous_data variable with the current data
        previous_data = current_data

    # Wait for 60 seconds before scraping the page again
    time.sleep(60)
