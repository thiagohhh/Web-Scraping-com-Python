import requests

# GET simples
response = requests.get("https://httpbin.org/get")
print(response.status_code)  # 200 = OK
print(response.text)          # conteúdo da página

# Com headers (simular navegador)
headers = {
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) Chrome/120"
}
response = requests.get("https://exemplo.com", headers=headers)

# POST (enviar dados)
data = {"usuario": "joao", "senha": "123"}
response = requests.post("https://api.exemplo.com/login", json=data)

# Verificar resposta
if response.status_code == 200:
    dados = response.json()  # se for JSON
    print(dados)
else:
    print(f"Erro: {response.status_code}")