import turtle
import random

aken = turtle.Screen()
pliiats = turtle.Turtle()
pliiats.speed(0)

def joonista_viisnurk():
    for _ in range(5):
        pliiats.forward(60)
        pliiats.right(72)

def joonista_ruut():
    for _ in range(4):
        pliiats.forward(60)
        pliiats.right(90)

def joonista_ring():
    pliiats.circle(30)

def joonista_kujund(kujund):
    if kujund == "viisnurk":
        joonista_viisnurk()
    elif kujund == "ruut":
        joonista_ruut()
    elif kujund == "ring":
        joonista_ring()

def vali_suvaline_kujund():
    return random.choice(["viisnurk", "ruut", "ring"])

# Peatsükkel
while True:
    valik = input("Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? ")
    if valik == "":
        print("Programm lõpetatud.")
        break

    mitu = input("Mitu kujundit soovid joonistada? ")
    if mitte := mitu.strip() == "":
        print("Programm lõpetatud.")
        break

    mitu = int(mitu)

    for _ in range(mitu):
        pliiats.penup()
        pliiats.goto(random.randint(-200, 200), random.randint(-200, 200))
        pliiats.pendown()

        kujund = valik if valik != "suvaline" else vali_suvaline_kujund()
        joonista_kujund(kujund)

print("Valmis!")
turtle.done()
