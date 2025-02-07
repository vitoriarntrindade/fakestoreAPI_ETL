import requests
from datetime import datetime

class FakeStoreAPI:
    BASE_URL = "https://fakestoreapi.com/products"

    @staticmethod
    def fetch_products():
        response = requests.get(FakeStoreAPI.BASE_URL)
        if response.status_code == 200:
            products = response.json()
            # Adiciona timestamp ao extrair
            for product in products:
                product["extracted_at"] = datetime.utcnow().isoformat()
            return products
        raise Exception(f"Erro ao buscar produtos: {response.status_code}")
