def contar_palavras(texto):
    # Remove pontuação simples e transforma em minúsculas
    pontuacoes = ".,!?;:\n"
    for p in pontuacoes:
        texto = texto.replace(p, " ")
    texto = texto.lower()

    palavras = texto.split()
    contagem = {}

    for palavra in palavras:
        if palavra in contagem:
            contagem[palavra] += 1
        else:
            contagem[palavra] = 1

    return contagem

# Exemplo de uso
texto_exemplo = """
Python é uma linguagem de programação poderosa. Python é fácil de aprender!
Python é muito popular entre desenvolvedores.
"""

resultado = contar_palavras(texto_exemplo)

# Exibir resultado
for palavra, quantidade in resultado.items():
    print(f"{palavra}: {quantidade}")
