def test_create_product(client):
    """Testa a criação de produtos via API ETL"""
    response = client.post("/api/products")
    
    assert response.status_code == 200 
    data = response.json()
    
    assert "message" in data
    assert  "produtos extraídos e salvos" in data["message"]


def test_get_products(client):
    """Testa a listagem de produtos"""
    
    # Primeiro, rodamos o ETL para garantir que existam produtos no banco
    client.post("/api/products")
    
    # Agora, testamos o GET /api/products
    response = client.get("/api/products")
    
    assert response.status_code == 200
    data = response.json()
    
    assert isinstance(data, list)
    assert len(data) > 0
    assert "name" in data[0]
