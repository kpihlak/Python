import turtle
import random

# Funktsioon, mis joonistab ruudu
def joonista_ruut():
    for _ in range(4):
        turtle.forward(50)
        turtle.left(90)

# Funktsioon, mis joonistab ringi
def joonista_ring():
    turtle.circle(50)

# Funktsioon, mis joonistab viisnurka
def joonista_viisnurk():
    for _ in range(5):
        turtle.forward(50)
        turtle.left(72)

# Funktsioon, mis joonistab suvalise kujundi
def joonista_suvaline_kujund():
    kujundid = [joonista_ruut, joonista_ring, joonista_viisnurk]
    random.choice(kujundid)()

# Funktsioon, mis küsib kasutajalt sisendi ja joonistab kujundid
def joonista_kujund():
    while True:
        # Küsi kasutajalt kujundi tüüp ja arv
        kujund = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? ").lower()
        if kujund not in ["viisnurk", "ring", "ruut", "suvaline"]:
            print("Vale sisend! Palun vali üks järgmistest: viisnurk, ring, ruut, suvaline.")
            continue
        try:
            arv = int(input("Mitu kujundit soovid joonistada? "))
            if arv <= 0:
                print("Arv peab olema positiivne!")
                continue
        except ValueError:
            print("Palun sisesta kehtiv number!")
            continue
        print("Joonistatakse kujundeid...")

        # Joonista kujundid vastavalt sisendile
        for _ in range(arv):
            x = random.randint(-200, 200)  # Suvaline X asukoht
            y = random.randint(-200, 200)  # Suvaline Y asukoht
            print(f"Joonistatakse kujund {x},{y}asukahas.")
            turtle.penup()
            turtle.goto(x, y)
            turtle.pendown()

            if kujund == "viisnurk":
                joonista_viisnurk()
            elif kujund == "ring":
                joonista_ring()
            elif kujund == "ruut":
                joonista_ruut()
            elif kujund == "suvaline":
                joonista_suvaline_kujund()

        # Küsi kasutajalt, kas ta tahab uuesti proovida või lõpetada
        uus_ake = input("Soovid joonistada uusi kujundeid? (jah / ei): ").lower()
        if uus_ake != "jah":
            break
        else:
            turtle.clear()  # Kustuta eelnevad kujundid enne uut joonistamist

    turtle.done()

# Käivita programm
turtle.speed(0)
joonista_kujund()
