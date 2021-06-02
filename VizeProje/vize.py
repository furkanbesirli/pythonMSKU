
print("Magazamiza Hos Geldiniz...")


aksiyonListesi = ["Maneater - 61TL", "Biomutant - 300TL",
                  "Soulworker - 10", "Sea of Thieves - 60",
                  "RONIN Two Souls - 20TL", "Yakuza - 60TL",
                  "Graven - 60TL", "Riftdrifter - 10TL",
                  "The Black Hole - 32TL", "Lost Souls - 14TL"]
simulasyonListesi = ["Powerwash Simulator - 50TL", "SnowRunner - 150TL",
               "Al Drone Simulator - 45TL", "Vivid Knight - 25TL",
               "Farm Manager 2021 - 32TL", "Imagine Earth - 40TL",
               "Tennis Manager 2021 - 69TL", "MotoGp21 - 53TL",
               "Jetborne Racing - 18TL", "Operator - 2TL"]
sporListesi = ["CryoFall - 18TL", "Ranch - 40TL", "Torque Drift - Free",
               "SlappyBall - Free", "F1 2020 - 50TL",
               "Dirt 5 - 92TL", "NBA 2K2021 - 400TL", "Skate City - 25TL",
               "Descenders - 25TL", "FIFA 21 - 400TL"]

satinAl = 0
sepet = 0
while satinAl == 0:
    oyunDongu = 0
    listeSec = int(input("Lutfen incelemek istegidiniz listeyi seciniz...0 = Aksiyon1 = Spor2 = Simulasyon"))

    if listeSec == 0:
        for oyunlar in aksiyonListesi:
            oyunDongu += 1
            print("{} {}".format(oyunDongu, oyunlar))
        oyunNo = int(input("Lutfen sepete eklemek istediginiz urun numarasini giriniz..."))
        if oyunNo == 1:
            print(aksiyonListesi[0] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 61

        elif oyunNo == 2:
            print(aksiyonListesi[1] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 300

        elif oyunNo == 3:
            print(aksiyonListesi[2] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 10

        elif oyunNo == 4:
            print(aksiyonListesi[3] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 60

        elif oyunNo == 5:
            print(aksiyonListesi[4] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 20

        elif oyunNo == 6:
            print(aksiyonListesi[5] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 60

        elif oyunNo == 7:
            print(aksiyonListesi[6] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 60

        elif oyunNo == 8:
            print(aksiyonListesi[7] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 10

        elif oyunNo == 9:
            print(aksiyonListesi[8] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 32

        elif oyunNo == 10:
            print(aksiyonListesi[9] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 14





    elif listeSec == 1:
        for oyunlar in sporListesi:
            oyunDongu += 1
            print("{} {}".format(oyunDongu, oyunlar))
        oyunNo = int(input("Lutfen sepete eklemek istediginiz urun numarasini giriniz..."))
        if oyunNo == 1:
            print(sporListesi[0] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 50

        elif oyunNo == 2:
            print(sporListesi[1] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 150

        elif oyunNo == 3:
            print(sporListesi[2] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 45

        elif oyunNo == 4:
            print(sporListesi[3] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 25

        elif oyunNo == 5:
            print(sporListesi[4] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 32

        elif oyunNo == 6:
            print(sporListesi[5] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 40

        elif oyunNo == 7:
            print(sporListesi[6] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 69

        elif oyunNo == 8:
            print(sporListesi[7] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 53

        elif oyunNo == 9:
            print(sporListesi[8] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 18

        elif oyunNo == 10:
            print(sporListesi[9] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 2






    elif listeSec == 2:
        for oyunlar in simulasyonListesi:
            oyunDongu += 1
            print("{} {}".format(oyunDongu, oyunlar))
        oyunNo = int(input("Lutfen sepete eklemek istediginiz urun numarasini giriniz..."))
        if oyunNo == 1:
            print(simulasyonListesi[0] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 18

        elif oyunNo == 2:
            print(simulasyonListesi[1] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 40

        elif oyunNo == 3:
            print(simulasyonListesi[2] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 0

        elif oyunNo == 4:
            print(simulasyonListesi[3] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 0

        elif oyunNo == 5:
            print(simulasyonListesi[4] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 50

        elif oyunNo == 6:
            print(simulasyonListesi[5] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 92

        elif oyunNo == 7:
            print(simulasyonListesi[6] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 400

        elif oyunNo == 8:
            print(simulasyonListesi[7] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 25

        elif oyunNo == 9:
            print(simulasyonListesi[8] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 25

        elif oyunNo == 10:
            print(simulasyonListesi[9] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")
            sepet += 400


    else:
        print("Program kapatiliyor. Gecerli bir liste secmediniz..!")
        satinAl = 1


















