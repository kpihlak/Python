
import turtle
import random

def ruut():
    for _ in range(4):        
         turtle.forward(50)
         turtle.left(90)

def ring():
   turtle.circle(50)

def viisnurk():
   for _ in range(5):
      turtle.forward(50)
      turtle.left(72)

def suvaline_kujund():
    kujundid = [ruut, ring, viisnurk]
    random.choice(kujundid)()
def joonista_kujund():
    while True:

        kujund  = input("Millist kujundit soovid joonistada (ruut, ring, viisnurk, suvaline_kujund)?").lower()
        if kujund not in ["ruut", "ring", "viisnurk", "suvaline"]:
            print("Vale sisend! Vali: ruut, ring, viisnurk, suvaline.")
            continue
        try:
        
            arv = int(input("Mitu kujundit soovid joonistada?"))
            if arv <=0:
                print("Arv peab olema positiivne!")
                continue
        
            for _ in range(arv):
                x = random.randint(-200, 200)
                y = random.randint(-200, 200)
                turtle.penup()
                turtle.goto(x,y)
                turtle.pendown()

            if kujund == "ruut":
                ruut()
            elif kujund =="ring":
                ring()
            elif kujund == "viisnurk":
                viisnurk()
            elif kujund == "suvaline_kujund":
                suvaline_kujund()
                
            uus_vaartus = input("Soovid joonistada uusi kujundeid? (jah/ei):").lower()
            if uus_vaartus != "jah":
                break
            else:
                turtle.clear()


            turtle.done()