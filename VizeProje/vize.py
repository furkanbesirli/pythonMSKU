
print("Magazamiza Hos Geldiniz...")


aksiyonListesi = ["das", "dsa", "dsad", "gsgd",  "hdfhf", "jfgnb", "", "gc", "q", "b"]
sporListesi = ["", "", "", "", "", "", "", "", "", ""]
simulasyonListesi = ["", "", "", "", "", "", "", "", "", ""]

satinAl = 0

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

        elif oyunNo == 2:
            print(aksiyonListesi[1] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 3:
            print(aksiyonListesi[2] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 4:
            print(aksiyonListesi[3] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 5:
            print(aksiyonListesi[4] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 6:
            print(aksiyonListesi[5] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 7:
            print(aksiyonListesi[6] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 8:
            print(aksiyonListesi[7] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 9:
            print(aksiyonListesi[8] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 10:
            print(aksiyonListesi[9] + " oyunu sayin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")





    elif listeSec == 1:
        for oyunlar in sporListesi:
            oyunDongu += 1
            print("{} {}".format(oyunDongu, oyunlar))
        oyunNo = int(input("Lutfen sepete eklemek istediginiz urun numarasini giriniz..."))
        if oyunNo == 1:
            print(sporListesi[0] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 2:
            print(sporListesi[1] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 3:
            print(sporListesi[2] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 4:
            print(sporListesi[3] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 5:
            print(sporListesi[4] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 6:
            print(sporListesi[5] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 7:
            print(sporListesi[6] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 8:
            print(sporListesi[7] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 9:
            print(sporListesi[8] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 10:
            print(sporListesi[9] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")






    elif listeSec == 2:
        for oyunlar in simulasyonListesi:
            oyunDongu += 1
            print("{} {}".format(oyunDongu, oyunlar))
        oyunNo = int(input("Lutfen sepete eklemek istediginiz urun numarasini giriniz..."))
        if oyunNo == 1:
            print(simulasyonListesi[0] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 2:
            print(simulasyonListesi[1] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 3:
            print(simulasyonListesi[2] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 4:
            print(simulasyonListesi[3] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 5:
            print(simulasyonListesi[4] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 6:
            print(simulasyonListesi[5] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 7:
            print(simulasyonListesi[6] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 8:
            print(simulasyonListesi[7] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 9:
            print(simulasyonListesi[8] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")

        elif oyunNo == 10:
            print(simulasyonListesi[9] + " oyunu satin aliniyor... (*******BURAYA FONSKIYON YAZILACAK*******)")


    else:
        print("Program kapatiliyor. Gecerli bir liste secmediniz..!")
        satinAl = 1


















