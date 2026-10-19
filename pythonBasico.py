# Variáveis e tipos
url = "https://exemplo.com"
paginas = 10
ativo = True

# Listas
resultados = []
resultados.append("dado1")
resultados.append("dado2")

# Dicionários
produto = {
    "nome": "Notebook",
    "preco": 3500.00,
    "disponivel": True
}

# Loops
for i in range(5):
    print(f"Página {i+1}")

# Funções
def limpar_texto(texto):
    return texto.strip().replace("\n", "")

# Try/Except (tratamento de erros)
try:
    resultado = 10 / 0
except ZeroDivisionError:
    print("Erro: divisão por zero!")
except Exception as e:
    print(f"Erro: {e}")