import turtle
import winsound
import os

# Obtém o caminho do diretório onde o script está sendo executado
script_dir = os.path.dirname(os.path.abspath(__file__))

# Constrói o caminho completo para o arquivo de som
sound_path = os.path.join(script_dir, 'som-raquete.wav')

wn = turtle.Screen()
wn.title("Ping Pong Game")
wn.bgcolor("black")
wn.setup(width=800, height=600)
wn.tracer(0)

# Placar
placar_1 = 0
placar_2 = 0


# Raquete 1
raquete_1 = turtle.Turtle()
raquete_1.speed(0)
raquete_1.shape("square")
raquete_1.shapesize(stretch_wid=5, stretch_len=1)
raquete_1.color("white")
raquete_1.penup()
raquete_1.goto(-350, 0)

# Raquete 2
raquete_2 = turtle.Turtle()
raquete_2.speed(0)
raquete_2.shape("square")
raquete_2.shapesize(stretch_wid=5, stretch_len=1)
raquete_2.color("white")
raquete_2.penup()
raquete_2.goto(350, 0)

# Bola
bola = turtle.Turtle()
bola.speed(0)
bola.shape("circle")
bola.color("white")
bola.penup()
bola.goto(0, 0)
bola.dx = 0.2
bola.dy = 0.2

# Placar
placar = turtle.Turtle()
placar.speed(0)
placar.color("white")
placar.penup()
placar.hideturtle()
placar.goto(0, 260)
placar.write("Jogador 1: 0     Jogador 2: 0", align="center", font=("Courier", 14, "normal"))

# Funções
def raquete_1_up():
    y = raquete_1.ycor()
    y += 20
    raquete_1.sety(y)

def raquete_1_down():
    y = raquete_1.ycor()
    y -= 20
    raquete_1.sety(y)


def raquete_2_up():
    y = raquete_2.ycor()
    y += 20
    raquete_2.sety(y)

def raquete_2_down():
    y = raquete_2.ycor()
    y -= 20
    raquete_2.sety(y)

# Teclas de funcionamento
wn.listen()
wn.onkeypress(raquete_1_up, "w")
wn.onkeypress(raquete_1_down, "s")
wn.onkeypress(raquete_2_up, "Up")
wn.onkeypress(raquete_2_down, "Down")

# Pro jogo rodar em loop

while True:
    wn.update()

    # Movimentação da bolinha
    bola.setx(bola.xcor() + bola.dx)
    bola.sety(bola.ycor() + bola.dy)

    # Pra checar a borda
    if bola.ycor() > 290:
        bola.sety(290)
        bola.dy *= -1

    if bola.ycor() < -290:
        bola.sety(-290)
        bola.dy *= -1
        
    if bola.xcor() > 390:
        bola.goto(0, 0)
        bola.dx *= -1
        placar_1 += 1
        placar.clear()
        placar.write(f"Jogador 1: {placar_1}     Jogador 2: {placar_2}", align="center", font=("Courier", 14, "normal"))

    if bola.xcor() < -390:
         bola.goto(0, 0)
         bola.dx *= -1
         placar_2 += 1
         placar.clear()
         placar.write(f"Jogador 1: {placar_1}     Jogador 2: {placar_2}", align="center", font=("Courier", 14, "normal"))
        
     # Pras raquetes baterem na bolinha
    if (bola.xcor() > 340 and bola.xcor() < 350) and (bola.ycor() < raquete_2.ycor() + 40 and bola.ycor() > raquete_2.ycor() -40):
         bola.setx(340)
         bola.dx *= -1
         winsound.PlaySound(sound_path, winsound.SND_ASYNC)
        
    if (bola.xcor() < -340 and bola.xcor() > -350) and (bola.ycor() < raquete_1.ycor() + 40 and bola.ycor() > raquete_1.ycor() -40):
        bola.setx(-340)
        bola.dx *= -1
        winsound.PlaySound(sound_path, winsound.SND_ASYNC)

