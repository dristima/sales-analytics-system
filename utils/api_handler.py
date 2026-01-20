import requests

def fetch_products(limit=30, skip=0):
    """
    Fetch products from DummyJSON API.

    Args:
        limit (int): number of products to fetch (default 30).
        skip (int): number of products to skip (for pagination).

    Returns:
        tuple: (products list, total count)
    """
    url = f"https://dummyjson.com/products?limit={limit}&skip={skip}"
    response = requests.get(url)
    data = response.json()
    return data['products'], data['total']

import requests

def fetch_products(limit=30, skip=0):
    url = f"https://dummyjson.com/products?limit={limit}&skip={skip}"
    response = requests.get(url)
    data = response.json()
    return data['products'], data['total']

def fetch_product_by_id(product_id):
    """
    Fetch a single product by ID from DummyJSON API.
    Returns: dict with product details
    """
    url = f"https://dummyjson.com/products/{product_id}"
    response = requests.get(url)
    product = response.json()
    return product

import requests

def fetch_products(limit=30, skip=0):
    """
    Fetch products from DummyJSON API.

    Args:
        limit (int): number of products to fetch (default 30).
        skip (int): number of products to skip (for pagination).

    Returns:
        tuple: (products list, total count)
    """
    url = f"https://dummyjson.com/products?limit={limit}&skip={skip}"
    response = requests.get(url)
    data = response.json()
    return data['products'], data['total']

import requests

def search_products(query):
    """
    Search products from DummyJSON API by keyword.

    Args:
        query (str): search term (e.g., 'phone', 'laptop', 'shoes')

    Returns:
        list: matching products
    """
    url = f"https://dummyjson.com/products/search?q={query}"
    response = requests.get(url)
    data = response.json()
    return data['products']