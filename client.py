import requests

BASE_URL = "http://127.0.0.1:8000"


def create_product(name, description, price):
    url = f"{BASE_URL}/products"
    data = {
        "name": name,
        "description": description,
        "price": price
    }
    response = requests.post(url, json=data)
    return response


def read_product(product_id):
    url = f"{BASE_URL}/products/{product_id}"
    response = requests.get(url)
    return response


def download_products():
    url = f"{BASE_URL}/products_download"
    response = requests.get(url)
    return response
