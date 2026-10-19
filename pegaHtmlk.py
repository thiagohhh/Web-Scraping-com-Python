from bs4 import BeautifulSoup
import requests

# 1. Buscar a página
url = "https://exemplo.com/produtos"
response = requests.get(url)
soup = BeautifulSoup(response.text, "html.parser")

# 2. Encontrar elementos
titulo = soup.find("h1").text
print(f"Título: {titulo}")

# Todos os links
links = soup.find_all("a")
for link in links:
    print(link.get("href"), link.text)

# Por classe CSS
precos = soup.find_all("span", class_="preco")
for p in precos:
    print(p.text)

# Por ID
elemento = soup.find(id="meu-elemento")

# Seletor CSS (como jQuery)
itens = soup.select("div.produto > h3")
for item in itens:
    print(item.text.strip())

# 3. Extrair tabela
tabela = soup.find("table")
linhas = tabela.find_all("tr")
for linha in linhas:
    colunas = linha.find_all("td")
    dados = [col.text.strip() for col in colunas]
    print(dados)