import requests

url = "http://localhost:8003/api/orders/"
data = {
    "customer_id": 1,
    "total_amount": 119.98,
    "order_date": "2025-06-17",
    "products_create": [
        {
            "product_id": 1,
            "quantity": 2
        },
        {
            "product_id": 2,
            "quantity": 1
        }
    ]
}

# En-têtes HTTP
headers = {
    "Content-Type": "application/json"
}

# Envoi de la requête POST
response = requests.post(url, json=data, headers=headers)

# Affichage du résultat
print("✅ Statut :", response.status_code)
try:
    print("📦 Réponse :", response.json())
except Exception:
    print("❌ Réponse non JSON :", response.text)
