import pytest
from app.adapters.fakestore import FakeStoreAPI


def test_fetch_products():
    products = FakeStoreAPI.fetch_products()
    assert isinstance(products, list)
    assert len(products) > 0
    assert "title" in products[0]
    assert "price" in products[0]
