from collections import Counter
import re

def contar_palavras(texto):
    # Usa expressão regular para extrair palavras, ignorando pontuação
    palavras = re.findall(r'\b\w+\b', texto.lower())
    return Counter(palavras)

# Exemplo de uso
texto_exemplo = """
A inteligência artificial está mudando o mundo. 
A inteligência por trás disso é impressionante!
"""

contagem = contar_palavras(texto_exemplo)

# Exibe as 5 palavras mais comuns
print("Palavras mais comuns:")
for palavra, quantidade in contagem.most_common(5):
    print(f"{palavra}: {quantidade}")
