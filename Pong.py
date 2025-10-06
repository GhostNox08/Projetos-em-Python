import turtle
import time

# Função para solicitar nomes dos jogadores
def get_player_names():
    player1_name = turtle.textinput("Nome do Jogador 1", "Digite seu nome:")
    player2_name = "Bot"  # O segundo jogador será o bot
    return player1_name, player2_name

# Criar tela
sc = turtle.Screen()
sc.title("Jogo Pong")
sc.bgcolor("white")
sc.setup(width=1000, height=600)

# Solicitar nomes dos jogadores
player1_name, player2_name = get_player_names()

# Paddle esquerdo (Jogador 1)
left_pad = turtle.Turtle()
left_pad.speed(0)
left_pad.shape("square")
left_pad.color("black")
left_pad.shapesize(stretch_wid=6, stretch_len=2)
left_pad.penup()
left_pad.goto(-400, 0)

# Paddle direito (Bot)
right_pad = turtle.Turtle()
right_pad.speed(0)
right_pad.shape("square")
right_pad.color("black")
right_pad.shapesize(stretch_wid=6, stretch_len=2)
right_pad.penup()
right_pad.goto(400, 0)

# Bola
hit_ball = turtle.Turtle()
hit_ball.speed(1)
hit_ball.shape("circle")
hit_ball.color("blue")
hit_ball.penup()
hit_ball.goto(0, 0)
hit_ball.dx = 5
hit_ball.dy = -5

# Inicializar pontuação
left_player = 0
right_player = 0

# Exibir pontuação
sketch = turtle.Turtle()
sketch.speed(0)
sketch.color("blue")
sketch.penup()
sketch.hideturtle()
sketch.goto(0, 260)
sketch.write(f"{player1_name}: 0 | {player2_name}: 0", align="center", font=("Courier", 24, "normal"))

# Funções para mover os paddles
def paddleaup():
    y = left_pad.ycor()
    if y < 250:
        y += 20
    left_pad.sety(y)

def paddleadown():
    y = left_pad.ycor()
    if y > -240:
        y -= 20
    left_pad.sety(y)

# Vincular teclas
sc.listen()
sc.onkeypress(paddleaup, "w")
sc.onkeypress(paddleadown, "s")

# Loop principal do jogo
while True:
    sc.update()
    time.sleep(0.01)

    # Movimento da bola
    hit_ball.setx(hit_ball.xcor() + hit_ball.dx)
    hit_ball.sety(hit_ball.ycor() + hit_ball.dy)

    # Verificar limites
    if hit_ball.ycor() > 290:
        hit_ball.sety(290)
        hit_ball.dy *= -1

    if hit_ball.ycor() < -290:
        hit_ball.sety(-290)
        hit_ball.dy *= -1

    # Verificar colisão com paddles
    if (hit_ball.xcor() > 390 and hit_ball.xcor() < 400) and (hit_ball.ycor() < right_pad.ycor() + 50 and hit_ball.ycor() > right_pad.ycor() - 50):
        hit_ball.setx(390)
        hit_ball.dx *= -1
        hit_ball.dx += 5.5  # Aumenta a velocidade da bola após a colisão

    if (hit_ball.xcor() < -390 and hit_ball.xcor() > -400) and (hit_ball.ycor() < left_pad.ycor() + 50 and hit_ball.ycor() > left_pad.ycor() - 50):
        hit_ball.setx(-390)
        hit_ball.dx *= -1
        hit_ball.dx += 5.5  # Aumenta a velocidade da bola após a colisão

    # Movimento do bot (paddle direito)
    if right_pad.ycor() < hit_ball.ycor() and hit_ball.dx > 0:
        right_pad.sety(right_pad.ycor() + 5.0)  # Aumenta a velocidade do bot
    elif right_pad.ycor() > hit_ball.ycor() and hit_ball.dx > 0:
        right_pad.sety(right_pad.ycor() - 5.0)  # Aumenta a velocidade do bot

    # Verificar se a bola saiu da tela
    if hit_ball.xcor() > 500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        left_player += 1
        sketch.clear()
        sketch.write(f"{player1_name}: {left_player} | {player2_name}: {right_player}", align="center", font=("Courier", 24, "normal"))

    if hit_ball.xcor() < -500:
        hit_ball.goto(0, 0)
        hit_ball.dy *= -1
        right_player += 1
        sketch.clear()
        sketch.write(f"{player1_name}: {left_player} | {player2_name}: {right_player}", align="center", font=("Courier", 24, "normal"))