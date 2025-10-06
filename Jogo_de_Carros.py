import random
import time

# Definição dos modelos de carro com atributos
carros = {
    "Carro de F1": {"velocidade": 10, "tracao": 10, "turbo": 10, "controle": 10, "freios": 10},
    "Picape": {"velocidade": 8, "tracao": 7, "turbo": 9, "controle": 6, "freios": 7},
    "SUV": {"velocidade": 7, "tracao": 9, "turbo": 6, "controle": 8, "freios": 9},
    "Porsche": {"velocidade": 9, "tracao": 6, "turbo": 9, "controle": 5, "freios": 9},
    "Fusca": {"velocidade": 6, "tracao": 9, "turbo": 4, "controle": 10, "freios": 10},
    "Carrinho de Compras": {"velocidade": 3, "tracao": 10, "turbo": 15, "controle": 2, "freios": 1},
    "Corsa": {"velocidade": 7, "tracao": 7, "turbo": 6, "controle": 8, "freios": 7},
    "Carro a Jato": {"velocidade": 15, "tracao": 8, "turbo": 20, "controle": 2, "freios": 16},
    "Skate": {"velocidade": 5, "tracao": 5, "turbo": 2, "controle": 4, "freios": 1},
    "Tesla": {"velocidade": 11, "tracao": 9, "turbo": 10, "controle": 10, "freios": 12},
    "Ford": {"velocidade": 7, "tracao": 6, "turbo": 2, "controle": 7, "freios": 8},
    "Ferrari": {"velocidade": 11, "tracao": 10, "turbo": 9, "controle": 8, "freios": 7},
    "Mustang": {"velocidade": 8, "tracao": 8, "turbo": 9, "controle": 7, "freios": 6},
"Bugatti": {"velocidade": 12, "tracao": 10, "turbo": 9, "controle": 11, "freios": 10},
"Opala": {"velocidade": 8, "tracao": 8, "turbo": 8, "controle": 8, "freios": 8},
"Jipe": {"velocidade": 7, "tracao": 4, "turbo": 3, "controle": 8, "freios": 9},
"Kombi": {"velocidade": 4, "tracao": 6, "turbo": 2, "controle": 8, "freios": 3},
"Lamborghini": {"velocidade": 9, "tracao": 8, "turbo": 8, "controle": 7, "freios": 6},
"Honda Civic": {"velocidade": 7, "tracao": 5, "turbo": 1, "controle": 6, "freios": 4},
"Moto": {"velocidade": 7, "tracao": 10, "turbo": 9, "controle": 4, "freios": 3},
"Citroen C3": {"velocidade": 7, "tracao": 8, "turbo": 5, "controle": 10, "freios": 8},
    
    
}

def escolher_carro(nome_jogador):
    print(f"\nEscolha o modelo de carro para {nome_jogador}:")
    for idx, carro in enumerate(carros.keys(), 1):
        print(f"{idx}. {carro}")
    escolha = int(input("Digite o número do carro escolhido: "))
    modelo = list(carros.keys())[escolha - 1]
    return modelo, carros[modelo]

def jogada_ia(atributos):
    avanco_base = random.randint(1, 10)
    avanco_total = avanco_base + (atributos["turbo"] // 2)
    return avanco_total

def evento_aleatorio():
    eventos = ["batida", "buraco", "óleo na pista",None]
    return random.choice(eventos)

def aplicar_evento(jogador, evento):
    if evento == "batida":
        print(f"{jogador} bateu! Ficará parado por 3 segundos.")
        time.sleep(1)
        return -5  # Penalidade de metros
    elif evento == "buraco":
        print(f"{jogador} caiu em um buraco! Avanço reduzido.")
        return -3  # Penalidade de metros
    elif evento == "óleo na pista":
        print(f"{jogador} escorregou no óleo! Avanço reduzido.")
        return -2  # Penalidade de metros
    return 0

def verificar_volta(distancia, volta_atual, metros_por_volta=100):
    if distancia >= metros_por_volta:
        volta_atual += 1
        distancia -= metros_por_volta
        print(f"Volta {volta_atual} completada!")
    return volta_atual, distancia

def verificar_evento_por_distancia(distancia, eventos_ocorridos, jogador):
    if distancia - eventos_ocorridos >= 50:  # Evento ocorre a cada 50 metros
        evento = evento_aleatorio()
        eventos_ocorridos += 50
        penalidade = aplicar_evento(jogador, evento)
        return penalidade, eventos_ocorridos
    return 0, eventos_ocorridos

def atualizar_posicoes(distancia_total1, distancia_total2, nome_jogador1, nome_jogador2):
    if distancia_total1 > distancia_total2:
        primeiro, segundo = nome_jogador1, nome_jogador2
    elif distancia_total2 > distancia_total1:
        primeiro, segundo = nome_jogador2, nome_jogador1
    else:
        primeiro, segundo = "Empatados", "Empatados"

    print(f"Posições atuais: 1º {primeiro}, 2º {segundo}")
    print(f"Distâncias totais: {nome_jogador1}: {distancia_total1} metros, {nome_jogador2}: {distancia_total2} metros")

def mensagem_vitoria(nome_vencedor, modelo, distancia_total):
    print(f"\nParabéns, {nome_vencedor}! Você venceu a corrida dirigindo um {modelo}! E percorreu um total de {distancia_total} metros!")

def calcular_velocidade_media(distancia_total, tempo_total):
    # Convertendo metros para quilômetros e segundos para horas
    distancia_km = distancia_total / 1000
    tempo_horas = tempo_total / 3600
    if tempo_horas == 0:
        return 0
    return distancia_km / tempo_horas

def corrida_carros():
    print("\nBem-vindo ao jogo de corrida de carros!\nO primeiro jogador que completar 3 voltas ganha!")
    nome_jogador1 = input('\nInsira o seu nome (Jogador 1): ')
    time.sleep(1)
    nome_jogador2 = input('Insira o nome do seu oponente (Jogador 2):')
    time.sleep(1)
    print(f'\nJogador 1: {nome_jogador1}\nJogador 2: {nome_jogador2}')
    time.sleep(3)

    # Escolha dos carros
    modelo_jogador1, atributos_jogador1 = escolher_carro(nome_jogador1)
    modelo_jogador2, atributos_jogador2 = escolher_carro(nome_jogador2)

    print(f"O jogador 1 ({nome_jogador1}) e o jogador 2 ({nome_jogador2}) estão se preparando para a corrida...")
    time.sleep(4)

    distancia_jogador1 = 0
    distancia_jogador2 = 0
    volta_jogador1 = 0
    volta_jogador2 = 0
    eventos_ocorridos_jogador1 = 0
    eventos_ocorridos_jogador2 = 0
    distancia_total_jogador1 = 0
    distancia_total_jogador2 = 0
    tempo_inicio = time.time()

    while volta_jogador1 < 3 and volta_jogador2 < 3:  # 3 voltas para vencer
        # Jogada jogador 1 (IA)
        avanco_jogador1 = jogada_ia(atributos_jogador1)
        penalidade, eventos_ocorridos_jogador1 = verificar_evento_por_distancia(distancia_jogador1, eventos_ocorridos_jogador1, nome_jogador1)
        distancia_jogador1 += avanco_jogador1 + penalidade
        distancia_total_jogador1 += avanco_jogador1 + penalidade
        volta_jogador1, distancia_jogador1 = verificar_volta(distancia_jogador1, volta_jogador1)

        # Jogada jogador 2 (IA)
        avanco_jogador2 = jogada_ia(atributos_jogador2)
        penalidade, eventos_ocorridos_jogador2 = verificar_evento_por_distancia(distancia_jogador2, eventos_ocorridos_jogador2, nome_jogador2)
        distancia_jogador2 += avanco_jogador2 + penalidade
        distancia_total_jogador2 += avanco_jogador2 + penalidade
        volta_jogador2, distancia_jogador2 = verificar_volta(distancia_jogador2, volta_jogador2)

        # Atualizar e exibir posições
        atualizar_posicoes(distancia_total_jogador1, distancia_total_jogador2, nome_jogador1, nome_jogador2)

        time.sleep(2)

    # Final do jogo
    tempo_total = time.time() - tempo_inicio
    if volta_jogador1 > volta_jogador2:
        mensagem_vitoria(nome_jogador1, modelo_jogador1, distancia_total_jogador1)
        velocidade_media_jogador1 = calcular_velocidade_media(distancia_total_jogador1, tempo_total)
        print(f"Velocidade média de {nome_jogador1}: {velocidade_media_jogador1:.2f} km/h")
    else:
        mensagem_vitoria(nome_jogador2, modelo_jogador2, distancia_total_jogador2)
        velocidade_media_jogador2 = calcular_velocidade_media(distancia_total_jogador2, tempo_total)
        print(f"Velocidade média de {nome_jogador2}: {velocidade_media_jogador2:.2f} km/h")

# Iniciar o jogo
corrida_carros()
