# PANGAKONTO
# Looge funktsioon, mis võimaldab lisada või eemaldada summasid pangakontolt. Funktsioon peaks algama algse saldoga ja võimaldama teha operatsioone:
# deposiit (raha lisamine)
# väljavõte (raha eemaldamine)
# Tagastage peale igat toimingut konto jääk .
# Funtsiooni parameetrid:
# algne_saldo: algse saldo väärtus
# toiming: String, mis tähistab tehtavat toimingut ('deposiit' või 'valjavote')
# summa: summa, mida soovitakse lisada või eemaldada

# def konto_haldur(algsaldo, toiming, summa):

#     if toiming =="deposiit":
#         algsaldo += summa
#     elif toiming =="valjavote":
#         if summa <= algsaldo:
#             algsaldo -= summa
#         else:
#          print("Ei ole piisavalt raha kontol.")
        
#     else:
#         print("Makse ei õnnestunud.")
#     return algsaldo
   
# saldo = 200
# print("Algsaldo:", saldo)

# saldo = konto_haldur(saldo, "deposiit", 50)
# print("Uus saldo pärast deposiiti", saldo)

# saldo = konto_haldur(saldo, "valjavote", 80)
# print("Uus saldo pärast väljavõtet:", saldo)

# saldo = konto_haldur(saldo, "valjavote", 150)
# print("Uus saldo peale raha liikumist:", saldo) 
   
        
# KILPKONN
# Kirjuta programm, mis lubab kasutajal valida kujundite tüübi (viisnurk, ring, ruut või suvaline) ja arvu. Programm joonistab seejärel antud arvu kujundeid valitud tüübiga või juhul, kui valik on “suvaline”, valib programm ise juhuslikult kujundi tüübi iga kujundi jaoks.
# Näide:
# Millist kujundit soovid joonistada (viisnurk, ring, ruut, suvaline)? Suvaline
# Mitu kujundit soovid joonistada? 5
# [Joonistab 5 kujundit, igaüks juhuslikult valitud tüübiga suvalistesse kohtadesse]
# Pärast joonistamist peaks programm pakkuma võimalust sisestada uued väärtused või väljuda programmist, jättes sisendi tühjaks.



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

            turtle.speed(0)
    joonista_kujund()

    