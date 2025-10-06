import random
import string

def gerar_senha(tamanho=5):
    caracteres = string.ascii_letters + string.digits + string.punctuation
    senha = ''.join(random.choice(caracteres) for i in range(tamanho))
    return senha

# Exemplo de uso
tamanho_da_senha = 10
senha_gerada = gerar_senha(tamanho_da_senha)
print(f'Senha gerada: {senha_gerada}')